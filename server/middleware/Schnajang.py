from fastapi import Request, HTTPException, status
from fastapi.responses import Response
from limbus.crypto import deobfuscate, obfuscate, generate_seed, decode_bytes


async def handle(req: Request, call_next):
    # Request middleware
    req_seed = req.headers.get("Content-Encrypted")

    if req_seed:
        try:
            deobfuscated_body = deobfuscate(await req.body(), int(req_seed))
            print("RECV:     " + decode_bytes(deobfuscated_body))
            req._body = deobfuscated_body

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error when deobfuscating request body: {e}",
            )

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing or empty 'Content-Encrypted' header",
        )

    # Response middleware
    try:
        res = await call_next(req)
        res_body = getattr(res, "body", b"".join([c async for c in res.body_iterator]))
        res_seed = generate_seed()
        print("SEND:     " + decode_bytes(res_body))
        obfuscated_body = obfuscate(res_body, res_seed)

        return Response(
            content=obfuscated_body,
            media_type="application/json",
            headers={"Content-Encrypted": str(res_seed)},
            status_code=res.status_code,
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error when obfuscating response body: {e}",
        )

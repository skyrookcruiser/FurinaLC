from fastapi import Request, HTTPException, status
from fastapi.responses import Response
from limbus.crypto import deobfuscate, obfuscate, generate_seed, decode_bytes


async def handle(req: Request, call_next):
    req_body = await req.body()
    req_seed = req.headers.get("Content-Encrypted")
    if req_seed:
        try:
            # Request
            deobfuscated_body = deobfuscate(req_body, int(req_seed))
            print("RECV:     " + decode_bytes(deobfuscated_body))
            req._body = deobfuscated_body

            # Response
            res = await call_next(req)
            res_body = getattr(
                res, "body", b"".join([c async for c in res.body_iterator])
            )
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
                detail=f"Error in middleware: {e}",
            )
    else:
        print("INFO:     " + "Request did not have a Content-Encrypted header.")
        print("RECV:     " + decode_bytes(req_body))
        res = await call_next(req)
        res_body = getattr(res, "body", b"".join([c async for c in res.body_iterator]))
        print("SEND:     " + decode_bytes(res_body))

        return Response(
            content=res_body,
            media_type="application/octet-stream",
            status_code=res.status_code,
        )

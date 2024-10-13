from fastapi import Request, HTTPException, status
from fastapi.responses import StreamingResponse, Response
from middleware.encryption import deobfuscate, obfuscate
import time


def unix_timestamp_seconds() -> int:
    return int(time.time())


async def handle(request: Request, call_next):
    encrypted_timestamp = request.headers.get("Content-Encrypted")

    if encrypted_timestamp:
        try:
            encrypted_timestamp = int(encrypted_timestamp)
            body = await request.body()
            decrypted_body = deobfuscate(body, encrypted_timestamp)

            if decrypted_body:
                print(f"\nREQ > {decrypted_body}")
                request._body = decrypted_body.encode()

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Decryption failed: {e}",
            )

    response = await call_next(request)
    response_timestamp = unix_timestamp_seconds()

    if response_timestamp:
        try:
            if isinstance(response, StreamingResponse):
                response_body = b"".join(
                    [chunk async for chunk in response.body_iterator]
                )
                print(f"\nRSP > {response_body}")
                encrypted_response = obfuscate(response_body, response_timestamp)

                return Response(
                    content=encrypted_response,
                    media_type="application/json",
                    headers={"Content-Encrypted": str(response_timestamp)},
                    status_code=status.HTTP_200_OK,
                )

            else:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Response failed: not a StreamingResponse",
                )

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Encryption failed: {e}",
            )

    return response

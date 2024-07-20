from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

API_KEY = "U2FpbGVzaEt1bWFy"
API_KEY_NAME = "Authorization"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def verify_token(api_key: str = Security(api_key_header)):
    if api_key == API_KEY:
        return True
    else:
        raise HTTPException(
            status_code=403,
            detail="Invalidate credentials",
        )

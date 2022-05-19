import jwt

from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from datetime import datetime, timedelta


class JWTHandler:
    security = HTTPBearer()

    def __init__(
        self, secret_key: str, expire_day: int = 364, algorithm: str = "HS256"
    ):
        self.secret_key: str = secret_key
        self.expire_day: int = expire_day
        self.algorithm: str = algorithm

    def create_access_token(self, subject):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=self.expire_day),
            "iat": datetime.utcnow(),
            "sub": subject,
        }
        return jwt.encode(
            payload,
            self.secret_key,
            algorithm=self.algorithm,
        )

    def decode_jwt_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Signature has expired",
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_jwt_token(auth.credentials)

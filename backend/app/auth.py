from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_pw: str, hashed_pw: str) -> bool:
    return pwd_context.verify(plain_pw, hashed_pw)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")  # remove dev-secret when moving to prod
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 60 * 12

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
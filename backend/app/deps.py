from fastapi import Depends, HTTPException, Header
from jose import JWTError
from sqlalchemy.orm import Session
from app.auth import decode_access_token
from app.database import get_db
from app import models
from app.crud import get_user_by_username

def get_current_user(authorization: str = Header(..., convert_underscores=False), db: Session = Depends(get_db)) -> models.WebAppUser:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization format")
    
    token = authorization.split("Bearer ")[1]
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = get_user_by_username(db, payload["sub"])
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user
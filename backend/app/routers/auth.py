from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.auth import verify_password, create_access_token
from app.crud import get_user_by_username

router = APIRouter()

@router.post("/login", response_model=schemas.TokenResponse)
def login(data: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_username(db, data.username)
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.username, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}
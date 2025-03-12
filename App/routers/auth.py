from fastapi import APIRouter, Depends, HTTPException
import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")

router = APIRouter(prefix="/auth", tags=["Authentication"])

def generate_token(user_id):
    payload = {
        "exp": datetime.utcnow() + timedelta(hours=1),
        "user_id": user_id
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

@router.post("/login")
def login(user: str, password: str):
    if user == "admin" and password == "1234":
        return {"token": generate_token(user)}
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")

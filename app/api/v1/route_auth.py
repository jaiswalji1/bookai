from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.auth import create_access_token
from app.core.security import hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

## dummy users roles
Users = {
    "admin": {"password": hash_password("admin123$"), "role": "admin"},
    "user": {"password": hash_password("user123$"), "role": "user"}
}

class AuthIn(BaseModel):
    username: str
    password: str

@router.post("/token")
async def token(payload: AuthIn):
    user = Users.get(payload.username)
    if not user or not verify_password(payload.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    token = create_access_token(payload.username, role=user["role"])
    return {"access_token": token, "token_type": "Bearer"}

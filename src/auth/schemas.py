from enum import Enum

from pydantic import BaseModel, EmailStr
from typing import Optional

class RoleEnum(str, Enum):
    USER = "user"
    ADMIN = "admin"

class RoleBase(BaseModel):
    id: int
    name: RoleEnum

class UserBase(BaseModel):
    # username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    role: RoleBase | None

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
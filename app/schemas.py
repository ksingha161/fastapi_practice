from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config():
        orm_mode = True

class UserLogin(UserCreate):
    pass
class ProductBase(BaseModel):
    product_type: str
    price: float
    is_purchased: bool = False


class PostProduct(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse
    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


# this is what user will input
class TokenData(BaseModel):
    id: Optional[str]

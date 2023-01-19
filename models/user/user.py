from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    password: str
    phone: str
    address: str
    wallet: int


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    phone: str
    address: str
    wallet: int


class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    password: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    wallet: Optional[int]

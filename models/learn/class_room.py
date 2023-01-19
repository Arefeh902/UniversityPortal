from pydantic import BaseModel
from typing import Optional


class ClassRoom(BaseModel):
    name: str


class ClassRoomCreate(BaseModel):
    name: str


class ClassRoomUpdate(BaseModel):
    name: Optional[str]

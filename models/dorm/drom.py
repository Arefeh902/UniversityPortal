from pydantic import BaseModel
from typing import Optional


class Dorm(BaseModel):
    id: int
    name: str
    dorm_class_id: int


class DormCreate(BaseModel):
    name: str
    dorm_class_id: int


class DormUpdate(BaseModel):
    id: int
    name: Optional[str]
    dorm_class_id: Optional[int]


class DormRoom(BaseModel):
    id: int
    dorm_id: int
    number: int
    capacity: int


class DormRoomCreate(BaseModel):
    dorm_id: int
    number: int
    capacity: int


class DormRoomUpdate(BaseModel):
    id: int
    dorm_id: Optional[int]
    number: Optional[int]
    capacity: Optional[int]


class StudentDormRoom(BaseModel):
    id: int
    student_id: int
    dorm_room: int


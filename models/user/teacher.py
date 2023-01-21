from pydantic import BaseModel
from datetime import date
from typing import Optional


class Teacher(BaseModel):
    id: int
    user_id: int
    start_date: date
    position: str
    username: str
    password: str
    is_heyatelmi: bool
    department: str


class TeacherCreate(BaseModel):
    user_id: int
    start_date: date
    position: str
    username: str
    password: str
    is_heyatelmi: bool
    department: str


class TeacherUpdate(BaseModel):
    user_id: Optional[int]
    start_date: Optional[date]
    position: Optional[str]
    is_heyatelmi: Optional[bool]
    department: Optional[str]

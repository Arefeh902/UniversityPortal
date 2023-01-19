from pydantic import BaseModel
from datetime import date
from typing import Optional


class Student(BaseModel):
    id: int
    user_id: int
    degree: int
    start_date: date
    membership_type: str
    ostad_moshaver: int
    department: str


class StudentCreate(BaseModel):
    user_id: int
    degree: int
    start_date: date
    membership_type: str
    ostad_moshaver: int
    department: str


class StudentUpdate(BaseModel):
    user_id: Optional[int]
    degree: Optional[int]
    start_date: Optional[date]
    membership_type: Optional[str]
    ostad_moshaver: Optional[int]
    department: Optional[str]

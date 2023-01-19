from pydantic import BaseModel
from typing import Optional


class PracticeClassRequest(BaseModel):
    id: int
    student_id: int
    section_id: int
    status: str


class PracticeClassRequestCreate(BaseModel):
    student_id: int
    section_id: int
    status: str


class PracticeClassRequestUpdate(BaseModel):
    id: int
    student_id: Optional[int]
    section_id: Optional[int]
    status: Optional[int]

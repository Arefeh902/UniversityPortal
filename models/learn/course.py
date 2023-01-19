from pydantic import BaseModel
from typing import Optional


class Course(BaseModel):
    id: int
    name: str
    suggested_term: int
    department: int


class CourseCreate(BaseModel):
    name: str
    suggested_term: int
    department: int


class CourseUpdate(BaseModel):
    id: int
    name: Optional[str]
    suggested_term: Optional[int]
    department: Optional[int]

from pydantic import BaseModel
from typing import Optional


class CoursePrerequisite(BaseModel):
    id: int
    before: int
    after: int
    is_prerequisite: bool


class CoursePrerequisiteCreate(BaseModel):
    before: int
    after: int
    is_prerequisite: bool


class CoursePrerequisiteUpdate(BaseModel):
    id: int
    before: Optional[int]
    after: Optional[int]
    is_prerequisite: Optional[bool]

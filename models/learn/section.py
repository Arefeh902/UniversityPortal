from pydantic import BaseModel
from typing import Optional
from datetime import time


class Section(BaseModel):
    id: int
    class_room: str
    course_id: int
    term_id: int


class SectionCreate(BaseModel):
    class_room: str
    course_id: int
    term_id: int


class SectionUpdate(BaseModel):
    class_room: Optional[str]
    course_id: Optional[int]
    term_id: Optional[int]


class SectionTime(BaseModel):
    id: int
    section_id: int
    week_day: int
    start_time: time
    end_time: time


class SectionTimeCreate(BaseModel):
    section_id: int
    week_day: int
    start_time: time
    end_time: time


class SectionTimeUpdate(BaseModel):
    section_id: Optional[int]
    week_day: Optional[int]
    start_time: Optional[time]
    end_time: Optional[time]


class StudentSection(BaseModel):
    id: int
    student_id: int
    section_id: int


class StudentSectionCreate(BaseModel):
    student_id: int
    section_id: int


class TeacherSection(BaseModel):
    id: int
    teacher_id: int
    section_id: int


class TeacherSectionCreate(BaseModel):
    id: int
    teacher_id: int
    section_id: int

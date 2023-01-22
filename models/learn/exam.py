from pydantic import BaseModel
from typing import Optional
from datetime import date, time


class Exam(BaseModel):
    id: int
    section_id: int
    exam_date: date
    start_at: time
    end_at: time
    type: str


class ExamCreate(BaseModel):
    section_id: int
    exam_date: date
    start_at: time
    end_at: time
    type: str

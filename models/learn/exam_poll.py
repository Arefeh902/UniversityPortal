from pydantic import BaseModel
from typing import Optional
from datetime import date, time, datetime


class ExamPoll(BaseModel):
    id: int
    starts_at: datetime
    ends_at: datetime
    section_id: int
    is_finial_exam: bool


class ExamPollCreate(BaseModel):
    starts_at: datetime
    ends_at: datetime
    section_id: int
    is_finial_exam: bool


class ExamPollUpdate(BaseModel):
    id: int
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    section_id: Optional[int]
    is_finial_exam: Optional[bool]


class ExamPollOption(BaseModel):
    id: int
    exam_poll_id: int
    exam_date: date
    starts_at: time
    ends_at: time


class ExamPollOptionCreate(BaseModel):
    exam_poll_id: int
    exam_date: date
    starts_at: time
    ends_at: time


class ExamPollOptionUpdate(BaseModel):
    id: int
    exam_poll_id: Optional[int]
    exam_date: Optional[date]
    starts_at: Optional[time]
    ends_at: Optional[time]


class ExamPollAnswer(BaseModel):
    id: int
    student_id: int
    exam_poll_option: int


class ExamPollAnswerCreate(BaseModel):
    student_id: int
    exam_poll_option: int


class ExamPollAnswerUpdate(BaseModel):
    id: int
    student_id: Optional[int]
    exam_poll_option: Optional[int]

from pydantic import BaseModel
from datetime import date
from typing import Optional


class Term(BaseModel):
    id: int
    title: str
    start_date: date
    end_date: date


class TermCreate(BaseModel):
    title: str
    start_date: date
    end_date: date


class TermUpdate(BaseModel):
    id: int
    title: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]

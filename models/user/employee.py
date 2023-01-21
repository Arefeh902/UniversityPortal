from pydantic import BaseModel
from datetime import date
from typing import Optional


class Employee(BaseModel):
    id: int
    user_id: int
    start_date: date
    position: str
    department: str


class EmployeeCreate(BaseModel):
    user_id: int
    start_date: date
    position: str
    department: str


class EmployeeUpdate(BaseModel):
    id: int
    user_id: Optional[int]
    start_date: Optional[date]
    position: Optional[str]
    department: Optional[str]

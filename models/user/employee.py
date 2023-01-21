from pydantic import BaseModel
from datetime import date
from typing import Optional


class Employee(BaseModel):
    id: int
    user_id: int
    start_date: date
    username: str
    password: str
    position: str
    department: str


class EmployeeCreate(BaseModel):
    user_id: int
    start_date: date
    username: str
    password: str
    position: str
    department: str


class EmployeeUpdate(BaseModel):
    user_id: Optional[int]
    start_date: Optional[date]
    username: str
    password: str
    position: Optional[str]
    department: Optional[str]

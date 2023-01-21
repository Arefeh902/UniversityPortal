from fastapi import APIRouter, Depends
from sqlalchemy import text
from db import get_session
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from models.learn.exam import Exam

router = APIRouter()


@router.post('/{section_id}/exam/create')
def create_exam(exam: Exam, section_id: int, db: Session = Depends(get_session)):
    query = text("INSERT INTO exam (section_id, exam_date, start_at, end_at, type) VALUES \
                ")
    result = db.execute(query, {"section_id": section_id}).all()
    return JSONResponse(content=result, status_code=200)



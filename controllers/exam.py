from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import text
from db import get_session
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from models.learn.exam import ExamCreate

router = APIRouter()


@router.post('/{section_id}/exam/create')
def create_exam(exam: ExamCreate, section_id: int, db: Session = Depends(get_session)):
    if exam.type == 'final':
        query = text("SELECT * FROM exam WHERE section_id=:section_id and type=:type")
        result = db.execute(query, {"section_id": section_id, "type": exam.type})
        if result is not None:
            raise HTTPException(status_code=401, detail="Final already exists")

    query = text("INSERT INTO exam (section_id, exam_date, start_at, end_at, type) VALUES \
                (:section_id, :exam_date, :start_at, :end_at, :type)")
    result = db.execute(query,
                        {"section_id": section_id,
                         "exam_date": exam.exam_date,
                         "start_at": exam.start_at,
                         "end_at": exam.end_at,
                         "type": exam.type
                         }).all()
    return JSONResponse(content=result, status_code=200)



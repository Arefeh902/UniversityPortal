from fastapi import APIRouter, Depends
from sqlalchemy import text
from db import get_session
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from models.user.student import Student

router = APIRouter()


@router.get('/{teacher_id}/detail')
def get_teacher_detail(teacher_id: int, db: Session = Depends(get_session)):
    query = text("SELECT * from teacher WHERE id:=teacher_id;")
    result = db.execute(query, {"teacher_id": teacher_id}).all()
    return JSONResponse(content=result, status_code=200)


@router.get('/{section_id}/practice-class-request/all')
def get_practice_class_requests(section_id: int, db: Session = Depends(get_session)):
    query = text("SELECT * from practice_class_request, student \
                WHERE student.id=practice_class_request.student_id and id:=section_id;")
    result = db.execute(query, {"section_id": section_id}).all()
    return JSONResponse(content=result, status_code=200)


@router.post('/{practice_class_request_id}/approve}')
def approve_practice_class_request(practice_class_request_id: int, db: Session = Depends(get_session)):
    query = text("UPDATE practice_class_request SET status:=status WHERE id:=request_id")
    result = db.execute(query, {"status": "Approved",
                                "request_id": practice_class_request_id}
                        ).all()
    return JSONResponse(content=result, status_code=200)


@router.post('/{practice_class_request_id}/cancel}')
def cancel_practice_class_request(practice_class_request_id: int, db: Session = Depends(get_session)):
    query = text("UPDATE practice_class_request SET status:=status WHERE id:=request_id")
    result = db.execute(query, {"status": "Canceled",
                                "request_id": practice_class_request_id}
                        ).all()
    return JSONResponse(content=result, status_code=200)

# start exam poll
@router.post('/{section_id}/exam-poll/create')
def create_exam_poll(exam_poll, section_id: int, db: Session = Depends(get_session)):
    pass


@router.get('{teacher_id}/advising-students')
def get_advising_students(teacher_id: int, db: Session = Depends(get_session)):
    query = text("SELECT * from student WHERE advisor_id:=teacher_id;")
    result = db.execute(query, {"teacher_id": teacher_id}).all()
    return JSONResponse(content=result, status_code=200)

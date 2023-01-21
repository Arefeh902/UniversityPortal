from fastapi import APIRouter, Depends
from sqlalchemy import text
from db import get_session
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from models.user.student import Student
from models.learn.section import Section

router = APIRouter()


@router.get('/{section_id}/detail')
def get_section_detail(section_id: int, db: Session = Depends(get_session())):
    query = text("SELECT * from section, course WHERE course.id=section.course_id and id:=section_id;")
    section_base = db.execute(query, {"section_id": section_id}).fetchone()
    query = text("SELECT * from section_time WHERE id:=section_id;")
    section_times = db.execute(query, {"section_id": section_id}).all()
    section_base += {"time": section_times}
    return JSONResponse(content=section_base, status_code=200)


@router.get('/{section_id}/teachers')
def get_section_detail(section_id: int, db: Session = Depends(get_session())):
    query = text("SELECT * from teacher__section WHERE id:=section_id;")
    result = db.execute(query, {"section_id": section_id}).all()
    return JSONResponse(content=result, status_code=200)


@router.get('/{section_id}/students')
def get_section_students(section_id: int, db: Session = Depends(get_session())):
    query = text("SELECT * from student__section WHERE id:=section_id;")
    result = db.execute(query, {"section_id": section_id}).all()
    return JSONResponse(content=result, status_code=200)


@router.get('/{section_id}/practice-class-request/all')
def get_practice_class_requests(section_id: int, db: Session = Depends(get_session())):
    query = text("SELECT * from practice_class_request, student \
                WHERE student.id=practice_class_request.student_id and id:=section_id;")
    result = db.execute(query, {"section_id": section_id}).all()
    return JSONResponse(content=result, status_code=200)


@router.get('/{section_id}/exam_poll/retrieve')
def get_exam_polls(section_id: int, db: Session = Depends(get_session())):
    query = text("SELECT * from practice_class_request, student \
                 WHERE student.id=practice_class_request.student_id and id:=section_id;")
    result = db.execute(query, {"section_id": section_id}).all()
    return JSONResponse(content=result, status_code=200)

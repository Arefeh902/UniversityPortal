from fastapi import APIRouter, Depends
from sqlalchemy import text
from db import get_session
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from models.user.student import Student

router = APIRouter()


@router.get('/{student_id}/terms')
def get_student_terms(student_id: int, db: Session = Depends(get_session)):
    query = text("SELECT * from student__term WHERE id:=student_id;")
    result = db.execute(query, {"student_id": student_id}).all()
    return JSONResponse(content=result, status_code=200)


@router.get('/{student_id}/details')
def get_student_detail(student_id: int, db: Session = Depends(get_session)):
    query = text("SELECT * from student WHERE id:=student_id;")
    result: Student = db.execute(query, {"student_id": student_id}).all()
    return JSONResponse(content=result, status_code=200)


@router.get('/{student_id}/section/all')
def get_all_student_sections(student_id: int, db: Session = Depends(get_session)):
    query = text("SELECT * from student__section WHERE id:=student_id;")
    result = db.execute(query, {"student_id": student_id}).all()
    return JSONResponse(content=result, status_code=200)


@router.get('/{student_id}/section/{term_id}')
def get_all_student_sections(student_id: int, term_id: int, db: Session = Depends(get_session)):
    query = text("SELECT * from student__section, section WHERE \
                student__section.id=section.id and id:=student_id and term.id=:term_id;")
    result = db.execute(query, {"student_id": student_id, "term_id": term_id}).all()
    return JSONResponse(content=result, status_code=200)


@router.post('/{student_id}/practice-class-request/{section_id}')
def create_practice_class_request(student_id: int, section_id: int, db: Session = Depends(get_session)):
    query = text("INSERT INTO practice_class_request (student_id, section_id, status\
                VALUES (:student_id, :section_id, :status);")
    result: Student = db.execute(query, {"student_id": student_id, "section_id": section_id, "status": "Pending"}).all()
    return JSONResponse(content=result, status_code=200)


@router.get('/{student_id}/practice-class-request/{section_id}')
def create_practice_class_request(student_id: int, section_id: int, db: Session = Depends(get_session)):
    query = text("INSERT INTO practice_class_request (student_id, section_id, status\
                VALUES (:student_id, :section_id, :status);")
    result: Student = db.execute(query, {"student_id": student_id, "section_id": section_id, "status": "Pending"}).all()
    return JSONResponse(content=result, status_code=200)

# get student deadlines (exams)

# course registration

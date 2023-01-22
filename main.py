from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session
from db import get_session
from router import api_router
from models.user.user import UserCreate, UserLogin, User
from models.user.teacher import Teacher
from models.user.student import Student
from models.user.employee import Employee
from fastapi.middleware.cors import CORSMiddleware


def get_application() -> FastAPI:
    _app = FastAPI()

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in ["http://localhost:8000", "https://localhost:8000", "http://localhost",
                                              "https://localhost"]],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
app.include_router(api_router)


@app.post('/login')
def login(user: UserLogin, db: Session = Depends(get_session)):
    query = text("SELECT * FROM public.user WHERE username = :username;")
    result: User = db.execute(query, {"username": user.username}).fetchone()
    if result is None:
        raise HTTPException(status_code=401, detail="Invalid username!")
    if user.password != result.password:
        raise HTTPException(status_code=401, detail="Invalid password!")

    query_student = text("SELECT * FROM student WHERE user_id=:user_id")
    students = db.execute(query_student, {"user_id": result.id}).all()
    query_teacher = text("SELECT * FROM teacher WHERE user_id=:user_id")
    teachers = db.execute(query_teacher, {"user_id": result.id}).all()
    query_employee = text("SELECT * FROM employee WHERE user_id=:user_id")
    employees = db.execute(query_employee, {"user_id": result.id}).all()

    result = dict(result)
    result = result | {
        "student_infos": students,
        "teacher_infos": teachers,
        "employee_infos": employees
    }

    return JSONResponse(content=result, status_code=200)


@app.post("/user/create/")
def create_user(user: UserCreate, db: Session = Depends(get_session)):
    query = text("SELECT * from public.user WHERE username=:username")
    result = db.execute(query, {"username": user.username}).fetchone()
    if not (result is None):
        raise HTTPException(status_code=404, detail="Username already exists!")
    query = text(
        "INSERT INTO public.user (first_name, last_name, username, password, phone, address) \
         VALUES (:first_name, :last_name, :username, :password, :phone, :address);"
    )
    db.execute(query,
               {"first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "password": user.password,
                "phone": user.phone,
                "address": user.address}
               )
    db.commit()
    return JSONResponse(content={}, status_code=201)

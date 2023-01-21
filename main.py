from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session
from db import get_session
# from sqlalchemy.sql import text
from router import api_router
from models.user.user import User, UserCreate, UserLogin
from models.user.teacher import Teacher
from models.user.student import Student
from models.user.employee import Employee


app = FastAPI()
app.include_router(api_router)


@app.post('/login')
def login(user: UserLogin, db: Session = Depends(get_session)):
    query = text("SELECT * FROM teacher WHERE username = :username;")
    result: Teacher = db.execute(query, {"username": user.username}).fetchone()
    if not (result is None):
        if user.password != result.password:
            raise HTTPException(status_code=401, detail="Invalid password!")
        return JSONResponse(content=result, status_code=200)
    query = text("SELECT * FROM student WHERE username = :username;")
    result: Student = db.execute(query, {"username": user.username}).fetchone()
    if not (result is None):
        if user.password != result.password:
            raise HTTPException(status_code=401, detail="Invalid password!")
        return JSONResponse(content=result, status_code=200)
    query = text("SELECT * FROM employee WHERE username = :username;")
    result: Employee = db.execute(query, {"username": user.username}).fetchone()
    if not (result is None):
        if user.password != result.password:
            raise HTTPException(status_code=401, detail="Invalid password!")
        return JSONResponse(content=result, status_code=200)
    raise HTTPException(status_code=401, detail="Invalid username!")



@app.post("/user/create/")
def create_user(user: UserCreate, db: Session = Depends(get_session)):
    query = text("SELECT * from student WHERE username=:username")
    result = db.execute(query, {"username": user.username}).fetchone()
    query1 = text("SELECT * from teacher WHERE username=:username")
    result1 = db.execute(query1, {"username": user.username}).fetchone()
    query2 = text("SELECT * from employee WHERE username=:username")
    result2 = db.execute(query2, {"username": user.username}).fetchone()
    if not (result is None and result1 is None and result2 is None):
        raise HTTPException(status_code=404, detail="Username already exists!")
    query = text(
        "INSERT INTO public.user (first_name, last_name, phone, address) \
         VALUES (:first_name, :last_name, :username, :password, :phone, :address, :wallet);"
    )
    db.execute(query,
               {"first_name": user.first_name,
                "last_name": user.last_name,
                "phone": user.phone,
                "address": user.address
               )
    db.commit()
    return JSONResponse(content={}, status_code=201)

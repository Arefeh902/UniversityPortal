from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session
from db import get_session
from router import api_router
from models.user.user import UserCreate, UserLogin
from models.user.teacher import Teacher
from models.user.student import Student
from models.user.employee import Employee


app = FastAPI()
app.include_router(api_router)


@app.post('/login')
def login(user: UserLogin, db: Session = Depends(get_session)):
    query = text("SELECT * FROM public.user WHERE username = :username;")
    result: Teacher = db.execute(query, {"username": user.username}).fetchone()
    if result is None:
        raise HTTPException(status_code=401, detail="Invalid username!")
    if user.password != result.password:
        raise HTTPException(status_code=401, detail="Invalid password!")

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

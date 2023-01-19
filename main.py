from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from sqlalchemy.orm import Session
from db import get_session
from sqlalchemy.sql import text
from pydantic import BaseModel
from router import api_router


app = FastAPI()
app.include_router(api_router)
get_session()

class User(BaseModel):
    username: str
    password: str


# in production you can use Settings management
# from pydantic to get secret key from .env
class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()


# # exception handler for authjwt
# # in production, you can tweak performance using orjson response
# @app.exception_handler(AuthJWTException)
# def authjwt_exception_handler(request: Request, exc: AuthJWTException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"detail": exc.message}
#     )


# provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token to use authorization
# later in endpoint protected
@app.post('/login')
def login(user: User, authorize: AuthJWT = Depends()):

    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Invalid Username!")
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Invalid password")

    # subject identifier for who this token is for example id or username from database
    access_token = authorize.create_access_token(subject=user.username)
    return {"access_token": access_token}


# protect endpoint with function jwt_required(), which requires
# a valid access token in the request headers to access.
@app.get('/user')
def user(authorize: AuthJWT = Depends()):
    authorize.jwt_required()`
    /
    current_user = authorize.get_jwt_subject()
    return {"user": current_user}


@app.post("/users/")
def create_user(user: User, db: Session = Depends(get_session)):
    query = text(
        "INSERT INTO users (email, name) VALUES (:email, :name)"
    )
    db.execute(query, email=user.username, name=user.username)
    db.commit()


@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_session)):
    query = text("SELECT * FROM users WHERE id = :user_id")
    result = db.execute(query, user_id=user_id).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": result["id"], "email": result["email"], "name": result["name"]}

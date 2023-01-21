from fastapi import APIRouter
from controllers import student, section


api_router = APIRouter()

api_router.include_router(student.router, prefix='/student', tags=['Student'])
api_router.include_router(section.router, prefix='/section', tags=['Section'])

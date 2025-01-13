from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.schemas.userChemas import UserCreateSchema,UserInLogin, UserWithToken, UserOutputSchema
from app.db.database import get_db
from app.service.userService import UserService
authRouter=APIRouter()

@authRouter.post('/login', status_code=200, response_model=UserWithToken)
def login(dataLogin:UserInLogin, session:Session=Depends(get_db)):
    try:
        return UserService(session=session).login(user_login_details=dataLogin)
    except Exception as e:
        print(e)
        raise e

@authRouter.post('/signup', status_code=200, response_model=UserOutputSchema)
def signUp(userData:UserCreateSchema, session:Session=Depends(get_db)):
    try:
        return UserService(session=session).signUp(user_details=userData)
    except Exception as e:
        print(e)
        raise e


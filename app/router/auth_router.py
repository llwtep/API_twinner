from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.schemas.userChemas import UserCreateSchema, UserInLogin, UserWithToken, UserOutputSchema
from app.db.database import get_db
from app.service.userService import UserService

authRouter = APIRouter()


@authRouter.post('/login', status_code=200, response_model=UserWithToken)
async def login(dataLogin: UserInLogin, session: AsyncSession = Depends(get_db)):
    try:
        return await UserService(session=session).login(user_login_details=dataLogin)
    except Exception as e:
        print(e)
        raise e


@authRouter.post('/signup', status_code=200, response_model=UserOutputSchema)
async def signUp(userData: UserCreateSchema, session: AsyncSession = Depends(get_db)):
    try:
        return await UserService(session=session).signUp(user_details=userData)
    except Exception as e:
        print(e)
        raise e


@authRouter.get('/all', status_code=200)
async def get_all_existing_users(session: AsyncSession = Depends(get_db)):
    try:
        return await UserService(session=session).get_all_users()
    except Exception as e:
        raise e

from app.db.repository.UserRepo import UserRepo
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.schemas.userChemas import UserCreateSchema, UserInLogin, UserWithToken
from app.security.hashHelper import hashHelper
from app.security.authHandler import authHandler


class UserService:
    def __init__(self, session: Session):
        self.__userRepo = UserRepo(session=session)

    def signUp(self, user_details: UserCreateSchema):
        if self.__userRepo.get_user_by_email(email=user_details.email):
            raise HTTPException(status_code=200, detail='Please sign in')
        hashed_password = hashHelper.get_hashed_password(plain_password=user_details.password)
        user_details.password = hashed_password
        return self.__userRepo.create_user(data_details=user_details)

    def login(self, user_login_details: UserInLogin):
        if not self.__userRepo.get_user_by_email(email=user_login_details.email):
            raise HTTPException(status_code=200, detail='Please sign up')
        user = self.__userRepo.get_user_by_email(email=user_login_details.email)
        if hashHelper.verify_password(plain_password=user_login_details.password, hashed_password=user.password):
            token = authHandler.sign_jwt(user_id=user.id)
            if token:
                return UserWithToken(token=token)
            raise HTTPException(status_code=500, detail='Unable process request')
        raise HTTPException(status_code=400, detail='Please check your credentials')

    def get_user_by_id(self, user_id: int):
        user = self.__userRepo.get_user_by_id(user_id)
        if user:
            return user
        raise HTTPException(status_code=400, detail='User is not available')

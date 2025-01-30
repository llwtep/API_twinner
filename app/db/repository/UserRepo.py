from sqlalchemy import select
from .BaseRepo import BaseRepo
from app.db.schemas.userChemas import UserCreateSchema, UserOutputSchema
from app.db.models.user import UserOrm


class UserRepo(BaseRepo):
    async def create_user(self, data_details: UserCreateSchema):
        new_user = UserOrm(**data_details.model_dump(exclude_none=True))
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(instance=new_user)
        return new_user

    async def user_exist_by_email(self, email: str) -> bool:
        result = await self.session.execute(
            select(UserOrm).filter_by(email=email)
        )
        user = result.scalars().first()
        if user:
            return True
        else:
            return False

    async def get_user_by_email(self, email: str):
        result = await self.session.execute(
            select(UserOrm).filter_by(email=email)
        )
        user = result.scalars().first()
        return user

    async def get_user_by_id(self, id: int):
        result = await self.session.execute(
            select(UserOrm).filter_by(id=id)
        )
        user = result.scalars().first()
        return user

    async def get_all_users(self):
        result = await self.session.execute(
            select(UserOrm)
        )
        users = result.scalars().all()
        return users

from .BaseRepo import BaseRepo
from app.db.schemas.userChemas import UserCreateSchema
from app.db.models.user import UserOrm


class UserRepo(BaseRepo):
    def create_user(self, data_details: UserCreateSchema):
        new_user = UserOrm(**data_details.model_dump(exclude_none=True))
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(instance=new_user)
        return new_user

    def user_exist_by_email(self, email: str) -> bool:
        user = self.session.query(UserOrm).filter_by(email=email).first()
        if user:
            return True
        else:
            return False

    def get_user_by_email(self, email: str):
        user = self.session.query(UserOrm).filter_by(email=email).first()
        return user

    def get_user_by_id(self, id: int):
        user = self.session.query(UserOrm).filter_by(id=id).first()
        return user

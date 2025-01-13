from typing import List

from ..database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship


class UserOrm(Base):
    __tablename__ = 'Users'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    posts: Mapped[List["PostsOrm"]] = relationship(back_populates='author')


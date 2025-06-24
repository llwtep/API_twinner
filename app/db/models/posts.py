from sqlalchemy import ForeignKey, func, text
from ..database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
import datetime


class PostsOrm(Base):
    __tablename__ = 'Posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('Users.id'))
    author: Mapped["UserOrm"] = relationship(back_populates='posts')
    title: Mapped[str]
    text_content: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

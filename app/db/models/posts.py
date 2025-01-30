from sqlalchemy import ForeignKey, text
from ..database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
import datetime


class PostsOrm(Base):
    __tablename__ = 'Posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('Users.id', ondelete='CASCADE'))
    author: Mapped["UserOrm"] = relationship(back_populates='posts')
    title: Mapped[str]
    text_content: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

import datetime

from pydantic import BaseModel, Field


class PostCreateSchema(BaseModel):
    author_id: int
    title: str = Field(max_length=256)
    text_content: str


class PostOutputSchema(PostCreateSchema):
    id: int
    created_at: datetime.datetime


class PostUpdateSchema(BaseModel):
    id: int
    author_id: int
    title: str | None = Field(max_length=256)
    text_content: str | None

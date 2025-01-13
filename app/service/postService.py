from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.repository.PostRepo import PostRepo
from app.db.schemas.postSchemas import PostCreateSchema, PostOutputSchema, PostUpdateSchema


class PostService:
    def __init__(self, session: Session):
        self.__postRepo = PostRepo(session=session)

    def add_post(self, post_data: PostCreateSchema):
        if self.__postRepo.exist_author_by_author_id(author_id=post_data.author_id):
            return self.__postRepo.create_post(post_data=post_data)
        else:
            raise HTTPException(status_code=500, detail='Author does not exist')

    def get_post_by_author_id(self, author_id: int):
        if self.__postRepo.exist_author_by_author_id(author_id=author_id):
            return self.__postRepo.exist_author_by_author_id(author_id=author_id)
        else:
            raise HTTPException(status_code=500, detail='Author does not exist')

    def get_post_by_id(self, post_id: int) -> PostOutputSchema:
        return self.__postRepo.get_post_by_id(post_id=post_id)

    def get_posts(self):
        return self.__postRepo.get_existing_posts()

    def post_update(self, post_id: int, data_updated: PostUpdateSchema):
        post = self.get_post_by_id(post_id)
        if post.author_id != data_updated.author_id:
            raise HTTPException(status_code=403, detail='You are not authorized to update this post')
        else:
            return self.__postRepo.update_post(post_id=post_id, updated_data=data_updated)

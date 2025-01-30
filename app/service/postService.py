from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.db.repository.PostRepo import PostRepo
from app.db.schemas.postSchemas import PostCreateSchema, PostOutputSchema, PostUpdateSchema


class PostService:
    def __init__(self, session: AsyncSession):
        self.__postRepo = PostRepo(session=session)

    async def add_post(self, post_data: PostCreateSchema):
        author_exist = await self.__postRepo.exist_author_by_author_id(author_id=post_data.author_id)
        if author_exist:
            return await self.__postRepo.create_post(post_data=post_data)
        else:
            raise HTTPException(status_code=500, detail='Author does not exist')

    async def get_post_by_author_id(self, author_id: int):
        author = await self.__postRepo.exist_author_by_author_id(author_id=author_id)
        if author:
            posts_by_author = await self.__postRepo.get_posts_by_author_id(author_id=author_id)
            return posts_by_author
        else:
            raise HTTPException(status_code=500, detail='Author does not exist')

    async def get_post_by_id(self, post_id: int) -> PostOutputSchema:
        return await self.__postRepo.get_post_by_id(post_id=post_id)

    async def get_posts(self):
        return await self.__postRepo.get_existing_posts()

    async def post_update(self, post_id: int, data_updated: PostUpdateSchema):
        post = await self.get_post_by_id(post_id)
        if post.author_id != data_updated.author_id:
            raise HTTPException(status_code=403, detail='You are not authorized to update this post')
        else:
            return await self.__postRepo.update_post(post_id=post_id, updated_data=data_updated)

    async def post_delete(self, post_id: int):
        return await self.__postRepo.delete_post_by_id(post_id=post_id)

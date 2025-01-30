from sqlalchemy import select
from .BaseRepo import BaseRepo
from app.db.schemas.postSchemas import PostCreateSchema,  PostUpdateSchema
from app.db.models.posts import PostsOrm
from app.db.models.user import UserOrm


class PostRepo(BaseRepo):
    async def create_post(self, post_data: PostCreateSchema):
        new_post = PostsOrm(**post_data.model_dump(exclude_none=True))
        self.session.add(new_post)
        await self.session.commit()
        await self.session.refresh(instance=new_post)
        return new_post

    async def get_post_by_id(self, post_id: int):
        result = await self.session.execute(
            select(PostsOrm).filter_by(id=post_id)
        )
        post = result.scalars().first()
        return post

    async def get_posts_by_author_id(self, author_id: int):
        result = await self.session.execute(
            select(PostsOrm).filter_by(author_id=author_id)
        )
        posts = result.scalars().all()
        return posts

    async def exist_author_by_author_id(self, author_id: int) -> bool:
        result = await self.session.execute(
            select(UserOrm).filter_by(id=author_id)
        )
        author = result.scalars().first()
        if author:
            return True
        else:
            return False

    async def get_existing_posts(self):
        result = await self.session.execute(select(PostsOrm))
        posts = result.scalars().all()
        return posts

    async def update_post(self, post_id: int, updated_data: PostUpdateSchema):
        result = await self.session.execute(
            select(PostsOrm).filter_by(id=post_id)
        )
        post = result.scalars().first()
        if updated_data.title:
            post.title = updated_data.title
        if updated_data.text_content:
            post.text_content = updated_data.text_content
        await self.session.commit()
        await self.session.refresh(instance=post)
        return post

    async def delete_post_by_id(self, post_id: int):
        result = await self.session.execute(
            select(PostsOrm).filter_by(id=post_id)
        )
        post_to_delete = result.scalars().first()
        await self.session.delete(post_to_delete)
        await self.session.commit()
        return {'success': True}

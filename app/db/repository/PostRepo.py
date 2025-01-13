from .BaseRepo import BaseRepo
from app.db.schemas.postSchemas import PostCreateSchema, PostOutputSchema, PostUpdateSchema
from app.db.models.posts import PostsOrm
from app.db.models.user import UserOrm


class PostRepo(BaseRepo):
    def create_post(self, post_data: PostCreateSchema):
        new_post = PostsOrm(**post_data.model_dump(exclude_none=True))
        self.session.add(new_post)
        self.session.commit()
        self.session.refresh(instance=new_post)

    def get_post_by_id(self, post_id: int):
        post = self.session.query(PostsOrm).filter_by(id=post_id).first()
        return post

    def get_posts_by_author_id(self, author_id: int):
        posts = self.session.query(PostsOrm).filter_by(author_id=author_id).all()
        return posts

    def exist_author_by_author_id(self, author_id: int) -> bool:
        author = self.session.query(UserOrm).filter_by(id=author_id).first()
        if author:
            return True
        else:
            return False

    def get_existing_posts(self):
        posts = self.session.query(PostsOrm).scalar().all()
        return posts

    def update_post(self, post_id: int, updated_data: PostUpdateSchema):
        post = self.session.query(PostsOrm).filter_by(id=post_id).first()
        if updated_data.title:
            post.title = updated_data.title
        if updated_data.text_content:
            post.text_content = updated_data.text_content
        self.session.commit()
        self.session.refresh(instance=post)
        return post

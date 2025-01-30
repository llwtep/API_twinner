from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.service.postService import PostService
from app.db.schemas.postSchemas import PostCreateSchema, PostOutputSchema, PostUpdateSchema

postRouter = APIRouter()


@postRouter.post('/create', status_code=200)
async def post_create(post_data: PostCreateSchema, session: AsyncSession = Depends(get_db)):
    try:
        return await PostService(session=session).add_post(post_data=post_data)
    except Exception as e:
        raise e


@postRouter.get('/all')
async def get_all_existing_posts(session: AsyncSession = Depends(get_db)):
    try:
        return await PostService(session=session).get_posts()
    except Exception as e:
        raise e


@postRouter.get('/{id}', status_code=200, response_model=PostOutputSchema)
async def post_get_by_id(id: int, session: AsyncSession = Depends(get_db)):
    try:
        return await PostService(session=session).get_post_by_id(post_id=id)
    except Exception as e:
        raise e


@postRouter.put('/update/{id}', status_code=200, response_model=PostOutputSchema)
async def update_post_by_id(id: int,
                            data: PostUpdateSchema,
                            session: AsyncSession = Depends(get_db)):
    try:
        return await PostService(session=session).post_update(post_id=id, data_updated=data)
    except Exception as e:
        raise e


@postRouter.delete('delete/{id}', status_code=200)
async def delete_post_by_id(id: int, session: AsyncSession = Depends(get_db)):
    try:
        return await PostService(session=session).post_delete(post_id=id)
    except Exception as e:
        raise e

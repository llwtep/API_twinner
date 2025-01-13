from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.service.postService import PostService
from app.db.schemas.postSchemas import PostCreateSchema, PostOutputSchema, PostUpdateSchema

postRouter = APIRouter()


@postRouter.post('/create', status_code=200,response_model=PostCreateSchema )
def post_create(post_data: PostCreateSchema, session: Session = Depends(get_db)):
    try:
        return PostService(session=session).add_post(post_data=post_data)
    except Exception as e:
        raise e


@postRouter.get('/{id}', status_code=200, response_model=PostOutputSchema)
def post_get_by_id(id: int, session: Session = Depends(get_db)):
    try:
        return PostService(session=session).get_post_by_id(post_id=id)
    except Exception as e:
        raise e


@postRouter.put('/update/{id}', status_code=200, response_model=PostOutputSchema)
def update_post_by_id(id: int, data: PostUpdateSchema, session: Session = Depends(get_db)):
    try:
        post_service=PostService(session=session)
        return PostService(session=session).post_update(post_id=id, data_updated=data)
    except Exception as e:
        raise e

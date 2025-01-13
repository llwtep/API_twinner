from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from app.utils.init_db import create_tables
from app.router.auth_router import authRouter
from app.db.schemas.userChemas import UserOutputSchema
from app.utils.protectRoute import get_current_user
from app.router.post_router import postRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print('Tables created')
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=authRouter, tags=['auth'], prefix='/auth')
app.include_router(router=postRouter, tags=['posts'], prefix='/post')


@app.get('/health')
def health_check():
    return {'status': 'Running...'}


@app.get('/protected')
def read_protected(user: UserOutputSchema = Depends(get_current_user)):
    return {'Top Secret': user}

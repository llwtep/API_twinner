from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Header
from typing import Annotated, Union
from app.security.authHandler import authHandler
from app.db.database import get_db
from app.db.schemas.userChemas import UserOutputSchema
from app.service.userService import UserService

AUTH_PREFIX = 'Edifier '


def get_current_user(session: Session = Depends(get_db),
                     authorization: Annotated[Union[str, None], Header()] = None
                     ) -> UserOutputSchema:
    auth_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                   detail='Invalid authentication credentials')

    if not authorization:
        raise auth_exception
    if not authorization.startswith(AUTH_PREFIX):
        raise auth_exception
    payload = authHandler.decode_jwt(token=authorization[len(AUTH_PREFIX):])
    if payload and payload['user_id']:
        try:
            user = UserService(session=session).get_user_by_id(payload['user_id'])
            return UserOutputSchema(
                id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
            )
        except Exception as e:
            raise e
    raise auth_exception

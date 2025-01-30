from decouple import config
import time
import jwt

JWT_SECRET = config('JWT_SECRET')
JWT_ALGORITHM = config('JWT_ALGORITHM')


class authHandler(object):
    @staticmethod
    def sign_jwt(user_id: int):
        payload = {
            'user_id': user_id,
            'expires': time.time() + 900
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return token

    @staticmethod
    def decode_jwt(token: str):
        try:
            decoded_payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            if 'expires' in decoded_payload and decoded_payload['expires'] >= time.time():
                return decoded_payload
            else:
                return None
        except jwt.ExpiredSignatureError:
            print('Token has expired')
        except jwt.InvalidTokenError:
            print('Invalid token')
        except Exception as e:
            print(f"Unable decode the token: {str(e)}")

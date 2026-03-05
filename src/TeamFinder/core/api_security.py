from datetime import datetime, timedelta

import bcrypt
import jwt

from .settings import settings


def hash_password(password: str) -> str:
    """Хэширование пароля"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """Проверка пароля с хэшем"""
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


def create_jwt_token(user_id: int, username: str) -> str:
    """Создание JWT токена"""
    payload = {
        "user_id": user_id,
        "username": username,
        "exp": datetime.now() + timedelta(minutes=90),
        "iat": datetime.now(),
    }
    token = jwt.encode(
        payload,
        key=settings.security.get_secret_key(),
        algorithm=settings.security.get_algorithm(),
    )
    return token


def verify_jwt_token(token: str) -> dict:
    """Проверка и декодирование JWT токена"""
    try:
        payload = jwt.decode(
            token,
            key=settings.security.get_secret_key(),
            algorithm=settings.security.get_algorithm(),
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")

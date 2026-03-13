```python
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

import jwt

from src.teamup.core import settings


class JWTHandler:
    """
    A utility class for handling JWT (JSON Web Tokens) in the application.
    """

    @staticmethod
    def create_access_token(
        data: Dict[str, Any], expires_delta: Optional[timedelta] = None
    ) -> str:
        """
        Creates an access token with the given data and expiration time.

        Args:
        - data: The payload data to be included in the token.
        - expires_delta: The expiration time of the token. Defaults to the value specified in the settings.

        Returns:
        - The generated access token.
        """
        to_encode = data.copy()
        expire = datetime.now() + (
            expires_delta
            or timedelta(minutes=settings.security.get_access_token_expires())
        )
        to_encode.update({"exp": expire, "type": "access"})
        return jwt.encode(
            to_encode,
            settings.security.get_secret_key(),
            algorithm=settings.security.get_algorithm(),
        )

    @staticmethod
    def create_refresh_token(data: Dict[str, Any]) -> str:
        """
        Creates a refresh token with the given data and expiration time.

        Args:
        - data: The payload data to be included in the token.

        Returns:
        - The generated refresh token.
        """
        to_encode = data.copy()
        expire = datetime.now() + timedelta(
            days=settings.security.get_refresh_token_expires()
        )
        to_encode.update({"exp": expire, "type": "refresh"})
        return jwt.encode(
            to_encode,
            settings.security.get_secret_key(),
            algorithm=settings.security.get_algorithm(),
        )

    @staticmethod
    def verify_token(token: str, token_type: str) -> Dict[str, Any] | None:
        """
        Verifies a token and returns its payload if it matches the given type.

        Args:
        - token: The token to be verified.
        - token_type: The expected type of the token.

        Returns:
        - The payload of the token if it matches the given type, otherwise None.
        """
        payload = JWTHandler.decode_token(token)
        if payload and payload.get("type") == token_type:
            return payload
        return None

    @staticmethod
    def decode_token(token: str) -> Dict[str, Any] | None:
        """
        Decodes a token and returns its payload.

        Args:
        - token: The token to be decoded.

        Returns:
        - The payload of the token if it's valid, otherwise None.
        """
        try:
            payload = jwt.decode(
                token,
                settings.security.get_secret_key(),
                algorithms=[settings.security.get_algorithm()],
            )
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    @staticmethod
    def get_token_data(user_id: UUID, username: str, role: str) -> Dict[str, str]:
        """
        Creates a payload for a JWT token.

        Args:
        - user_id: The ID of the user.
        - username: The username of the user.
        - role: The role of the user.

        Returns:
        - A dictionary containing the user's data.
        """
        return {"sub": str(user_id), "username": username, "role": role}
```
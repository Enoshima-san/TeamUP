```python
import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from ..enums import UserRole
from .announcement import Announcement
from .complaints import Complaints
from .player_rating import PlayerRating
from .response import Response
from .user_games import UserGames


@dataclass
class User:
    """
    Represents a user in the system.

    Attributes:
        email (str): The user's email address.
        username (str): The user's username.
        password_hash (str): The user's password hash.
        user_id (UUID): The user's unique identifier.
        registration_date (datetime): The date the user registered.
        last_login (datetime): The date the user last logged in.
        is_active (bool): Whether the user is currently active.
        role (str): The user's role in the system.
        has_microphone (bool): Whether the user has a microphone.
        age (Optional[int]): The user's age.
        about_me (Optional[str]): The user's description.
        is_blocked (bool): Whether the user is blocked.
        blocked_reason (Optional[str]): The reason the user was blocked.
        user_games (List[UserGames]): The user's games.
        user_ratings (List[PlayerRating]): The user's ratings.
        user_responses (List[Response]): The user's responses.
        user_announcements (List[Announcement]): The user's announcements.
        user_complaints (List[Complaints]): The user's complaints.
    """

    email: str
    username: str
    password_hash: str
    user_id: UUID = field(default_factory=uuid4)

    registration_date: datetime = field(default_factory=datetime.now)
    last_login: datetime = field(default_factory=datetime.now)
    is_active: bool = True
    role: str = UserRole.USER.value
    has_microphone: bool = False
    age: Optional[int] = None
    about_me: Optional[str] = None
    is_blocked: bool = False
    blocked_reason: Optional[str] = None

    user_games: List["UserGames"] = field(default_factory=list)
    user_ratings: List["PlayerRating"] = field(default_factory=list)
    user_responses: List["Response"] = field(default_factory=list)
    user_announcements: List["Announcement"] = field(default_factory=list)
    user_complaints: List["Complaints"] = field(default_factory=list)

    def set_username(self, username: str) -> None:
        """
        Sets the user's username.

        Args:
            username (str): The new username.

        Raises:
            ValueError: If the username is too short or too long.
        """
        if not username:
            raise ValueError("Username cannot be empty")
        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters long")
        if len(username) > 15:
            raise ValueError("Username cannot be longer than 15 characters")
        self.username = username

    def set_description(self, description: str) -> None:
        """
        Sets the user's description.

        Args:
            description (str): The new description.

        Raises:
            ValueError: If the description is too long.
        """
        if len(description) > 255:
            raise ValueError("Description cannot be longer than 255 characters")
        self.about_me = description

    def go_online(self) -> None:
        """
        Marks the user as online.
        """
        self.is_active = True

    def go_offline(self) -> None:
        """
        Marks the user as offline.
        """
        self.is_active = False

    def block(self, reason: str) -> None:
        """
        Blocks the user.

        Args:
            reason (str): The reason for blocking the user.

        Raises:
            ValueError: If the user is already blocked or the reason is empty.
        """
        if self.is_blocked:
            raise ValueError("User is already blocked")
        if not reason:
            raise ValueError("Reason for blocking is required")

        self.is_blocked = True
        self.blocked_reason = reason

    def unblock(self) -> None:
        """
        Unblocks the user.
        """
        if not self.is_blocked:
            raise ValueError("User is not blocked")

        self.is_blocked = False
        self.blocked_reason = None

    def is_admin(self) -> bool:
        """
        Checks if the user is an admin.

        Returns:
            bool: Whether the user is an admin.
        """
        return self.role == UserRole.ADMIN.value

    def add_game(self, game_id: UUID) -> "UserGames":
        """
        Adds a game to the user's list of games.

        Args:
            game_id (UUID): The ID of the game to add.

        Returns:
            UserGames: The newly added game.

        Raises:
            ValueError: If the game is already added.
        """
        if any(ug.game_id == game_id for ug in self.user_games):
            raise ValueError("Game is already added to user's games")
        user_game = UserGames(user_id=self.user_id, game_id=game_id)
        self.user_games.append(user_game)
        return user_game

    def remove_game(self, game_id: UUID) -> None:
        """
        Removes a game from the user's list of games.

        Args:
            game_id (UUID): The ID of the game to remove.
        """
        self.user_games = [ug for ug in self.user_games if ug.game_id != game_id]

    @staticmethod
    def create(
        email: str,
        username: str,
        password_hash: str,
        age: Optional[int] = None,
        role: str = UserRole.USER.value,
        about_me: Optional[str] = None,
        blocked_reason: Optional[str] = None,
        registration_date: datetime = datetime.now(),
        last_login: datetime = datetime.now(),
        is_active: bool = True,
        is_blocked: bool = False,
    ) -> "User":
        """
        Creates a new user.

        Args:
            email (str): The user's email address.
            username (str): The user's username.
            password_hash (str): The user's password hash.
            age (Optional[int]): The user's age.
            role (str): The user's role.
            about_me (Optional[str]): The user's description.
            blocked_reason (Optional[str]): The reason the user was blocked.
            registration_date (datetime): The date the user registered.
            last_login (datetime): The date the user last logged in.
            is_active (bool): Whether the user is active.
            is_blocked (bool): Whether the user is blocked.

        Returns:
            User: The newly created user.

        Raises:
            ValueError: If the email is invalid or the username is too short or too long.
        """
        if not email or "@" not in email or len(email) > 255 or not re.match(
            r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email
        ):
            raise ValueError("Invalid email")
        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters long")
        if len(username) > 15:
            raise ValueError("Username cannot be longer than 15 characters")

        return User(
            email=email,
            username=username,
            password_hash=password_hash,
            age=age,
            role=role,
            about_me=about_me,
            is_active=is_active,
            is_blocked=is_blocked,
            blocked_reason=blocked_reason,
            registration_date=registration_date,
            last_login=last_login,
        )
```
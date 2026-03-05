from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from .announcement import Announcement
from .complaint import Complaint
from .player_raiting import PlayerRaiting
from .response import Response
from .user_game import UserGame


@dataclass
class User:
    email: str
    username: str
    password_hash: str
    user_id: UUID = field(default_factory=uuid4)

    age: Optional[int] = None
    about_me: Optional[str] = None
    blocked_reason: Optional[str] = None
    registration_date: datetime = field(default_factory=datetime.now)
    last_login: datetime = field(default_factory=datetime.now)
    is_active: bool = True
    role: str = "user"
    is_blocked: bool = False

    user_games: List["UserGame"] = field(default_factory=list)
    user_raitings: List["PlayerRaiting"] = field(default_factory=list)
    user_responses: List["Response"] = field(default_factory=list)
    user_announcements: List["Announcement"] = field(default_factory=list)
    user_complaints: List["Complaint"] = field(default_factory=list)

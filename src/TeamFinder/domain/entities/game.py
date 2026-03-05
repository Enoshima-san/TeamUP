from dataclasses import dataclass, field
from typing import List
from uuid import UUID, uuid4

from .announcement import Announcement
from .player_raiting import PlayerRaiting
from .rank import Rank
from .user_game import UserGame


@dataclass
class Game:
    game_name: str
    icon: bytes
    game_id: UUID = field(default_factory=uuid4)

    game_announcements: List["Announcement"] = field(default_factory=list)
    game_ranks: List["Rank"] = field(default_factory=list)
    game_players: List["UserGame"] = field(default_factory=list)
    game_player_ratings: List["PlayerRaiting"] = field(default_factory=list)

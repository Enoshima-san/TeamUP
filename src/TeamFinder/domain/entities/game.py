from dataclasses import dataclass, field
from typing import List
from uuid import UUID, uuid4

from .announcement import Announcement
from .player_raiting import PlayerRating
from .rank import Rank
from .user_games import UserGames


@dataclass
class Game:
    game_name: str
    icon: bytes
    game_id: UUID = field(default_factory=uuid4)

    game_announcements: List["Announcement"] = field(default_factory=list)
    game_ranks: List["Rank"] = field(default_factory=list)
    game_players: List["UserGames"] = field(default_factory=list)
    game_player_ratings: List["PlayerRating"] = field(default_factory=list)

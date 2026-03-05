from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class PlayerRaiting:
    user_id: UUID
    game_id: UUID
    response_id: UUID
    raiting_id: UUID = field(default_factory=uuid4)

    raiting_value: int = 0
    created_at: datetime = field(default_factory=datetime.now)

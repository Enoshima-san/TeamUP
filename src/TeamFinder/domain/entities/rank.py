from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Rank:
    game_id: UUID
    rank_name: str
    rank_level: int  # полагаю кол-во ММР
    rank_id: UUID = field(default_factory=uuid4)

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from .complaint import Complaint


@dataclass
class Announcement:
    user_id: UUID
    game_id: UUID
    announcement_id: UUID = field(default_factory=uuid4)

    rank_min: Optional[int] = None
    rank_max: Optional[int] = None
    description: Optional[str] = None
    # ['активный', 'приотсановлен', 'завершен']
    status: str = "активный"
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    announcement_complaints: List["Complaint"] = field(default_factory=list)

from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from .complaint import Complaint


@dataclass
class Response:
    announcement_id: UUID
    user_id: UUID
    response_id: UUID = field(default_factory=uuid4)
    # ['на рассмотрении', 'отклонен', 'принят']
    status: str = "на расмотрении"
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    response_complaints: List["Complaint"] = field(default_factory=list)

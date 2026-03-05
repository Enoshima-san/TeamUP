from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class UserGame:
    user_id: UUID
    game_id: UUID
    user_game_id: UUID = field(default_factory=uuid4)

    preferred: bool = False

    def toggle_preferred(self):
        self.preferred = not self.preferred

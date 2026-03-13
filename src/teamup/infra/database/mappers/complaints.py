```python
from src.teamup.domain import Complaints
from ..models import ComplaintsORM

class ComplaintsMapper:
    """
    Mapper class responsible for converting between Complaints domain objects and ComplaintsORM database objects.
    """

    @staticmethod
    def to_domain(orm: ComplaintsORM | None) -> Complaints:
        """
        Converts a ComplaintsORM database object to a Complaints domain object.

        Args:
            orm: The ComplaintsORM database object to convert.

        Returns:
            The converted Complaints domain object.

        Raises:
            ValueError: If the ORM object is None.
        """
        if not orm:
            raise ValueError("ORM object is None")

        return Complaints(
            complaint_id=orm.complaint_id,
            user_id=orm.user_id,
            announcement_id=orm.announcement_id,
            response_id=orm.response_id,
            status=orm.status,
            created_at=orm.created_at,
            resolved_at=orm.resolved_at,
        )

    @staticmethod
    def to_orm(entity: Complaints | None) -> ComplaintsORM:
        """
        Converts a Complaints domain object to a ComplaintsORM database object.

        Args:
            entity: The Complaints domain object to convert.

        Returns:
            The converted ComplaintsORM database object.

        Raises:
            ValueError: If the entity is None.
        """
        if not entity:
            raise ValueError("Entity is None")

        return ComplaintsORM(
            complaint_id=entity.complaint_id,
            user_id=entity.user_id,
            announcement_id=entity.announcement_id,
            response_id=entity.response_id,
            status=entity.status,
            created_at=entity.created_at,
            resolved_at=entity.resolved_at,
        )
```
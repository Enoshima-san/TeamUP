from src.teamup.domain import Complaints

from ..models import ComplaintsORM


class ComplaintsMapper:
    @staticmethod
    def to_domain(orm: ComplaintsORM | None) -> Complaints:
        if not orm:
            raise ValueError("ORM object is None")

        return Complaints(
            complaint_id=orm.complaint_id,  # type: ignore[reportArgumentType]
            user_id=orm.user_id,  # type: ignore[reportArgumentType]
            announcement_id=orm.announcement_id,  # type: ignore[reportArgumentType]
            response_id=orm.response_id,  # type: ignore[reportArgumentType]
            status=orm.status,  # type: ignore[reportArgumentType]
            created_at=orm.created_at,  # type: ignore[reportArgumentType]
            resolved_at=orm.resolved_at,  # type: ignore[reportArgumentType]
        )

    @staticmethod
    def to_orm(entity: Complaints | None) -> ComplaintsORM:
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

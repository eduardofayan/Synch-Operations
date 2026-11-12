from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base


class Schedule(Base):

    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    automation_id: Mapped[int] = mapped_column(
        ForeignKey("automations.id")
    )

    cron_expression: Mapped[str] = mapped_column(
        String(100)
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    automation = relationship(
        "Automation"
    )
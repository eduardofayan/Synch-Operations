from datetime import datetime

from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base

# Classe que representa um agente no sistema
class Agent(Base):

    __tablename__ = "agents"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    machine_name: Mapped[str] = mapped_column(
        String(150)
    )

    version: Mapped[str] = mapped_column(
        String(20)
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="offline"
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    last_heartbeat: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True
    )
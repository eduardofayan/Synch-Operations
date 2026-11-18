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
        String(100),
        nullable=False
    )

    machine_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    version: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="offline",
        nullable=False
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    last_heartbeat: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )
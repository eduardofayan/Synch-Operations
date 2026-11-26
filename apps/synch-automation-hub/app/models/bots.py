from datetime import datetime

from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base

from typing import Optional

# Classe que representa um bot no sistema
class Bot(Base):

    # Nome da tabela no banco de dados que representa os bots
    __tablename__ = "bots"

    # Identificador único do bot
    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    # Nome do bot
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Nome da máquina onde o bot está rodando
    machine_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        unique=True
)
    
    # Versão do bot
    version: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    # Status do bot (online/offline) 
    status: Mapped[str] = mapped_column(
        String(20),
        default="offline",
        nullable=False
    )

    # Indica se o bot está ativo
    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    # Último heartbeat recebido do bot com base no fuso horário do banco de dados
    last_heartbeat: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
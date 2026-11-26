from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.bot import (BotRegister)
from app.services.bot_service import ( BotService)

""" 
    API para gerenciar operações relacionadas a bots.
    Inclui endpoints para registrar bots, listar bots e atualizar o heartbeat.
 """

# Roteador para endpoints relacionados a bots
router = APIRouter(
    prefix="/api/v1/bots",
    tags=["Bots"]
)

# Endpoint para registrar um novo bot
@router.post("/register")
def register_bot(
    bot: BotRegister,
    db: Session = Depends(get_db)
):

    result = BotService.register(
        db,
        bot
    )

    return {
        "id": result["bot"].id,
        "created": result["created"],
        "status": (
            "registered"
            if result["created"]
            else "existing"
        )
    }

# Endpoint para listar todos os bots registrados no sistema
@router.get("/")
def list_bots(
    db: Session = Depends(get_db)
):

    return BotService.list_all(db)

# Endpoint para atualizar o heartbeat de um bot específico
@router.post("/{bot_id}/heartbeat")
def heartbeat(
    bot_id: int,
    db: Session = Depends(get_db)
):

    bot = BotService.heartbeat(
        db,
        bot_id
    )

    if not bot:
        return {
            "status": "not_found"
        }

    return {
        "status": "received"
    }

# Endpoint para buscar bots por nome da máquina
@router.get("/machine/{machine_name}")
def get_by_machine_name(
    machine_name: str,
    db: Session = Depends(get_db)
):
    return BotService.get_by_machine_name(
        db,
        machine_name
    )

# Endpoint para listar os jobs de um bot específico
@router.get("/{bot_id}/jobs")
def get_jobs(
    bot_id: int
):
    return []
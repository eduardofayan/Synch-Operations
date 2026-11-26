from app.models.bots import Bot
from datetime import datetime

# Repositório para operações de banco de dados relacionadas a bots
class BotRepository:

    # Cria um novo bot no banco de dados
    @staticmethod
    def create_or_get(
        db,
        bot_data
    ):

        existing = (
            db.query(Bot)
            .filter(
                Bot.machine_name ==
                bot_data.machine_name
            )
            .first()
        )

        if existing:
            return {
                "bot": existing,
                "created": False
            }

        bot = Bot(
            name=bot_data.name,
            machine_name=bot_data.machine_name,
            version=bot_data.version,
            status="online"
        )

        db.add(bot)

        db.commit()

        db.refresh(bot)

        return {
            "bot": bot,
            "created": True
        }
    # Obtém todos os bots do banco de dados
    @staticmethod
    def get_all(db):

        return db.query(Bot).all()

    # Obtém um bot pelo ID
    @staticmethod
    def get_by_id(
        db,
        bot_id: int
    ):

        return (
            db.query(Bot)
            .filter(Bot.id == bot_id)
            .first()
        )

    @staticmethod
    def update_heartbeat(
        db,
        bot_id: int
    ):

        bot = (
            db.query(Bot)
            .filter(Bot.id == bot_id)
            .first()
        )

        if not bot:
            return None

        bot.last_heartbeat = datetime.utcnow()

        bot.status = "online"

        db.commit()
        db.refresh(bot)

        return bot

    # Obtém um bot pelo nome da máquina
    @staticmethod
    def get_by_machine_name(
        db,
        machine_name: str
    ):

        return (
            db.query(Bot)
            .filter(
                Bot.machine_name == machine_name
            )
            .first()
        )
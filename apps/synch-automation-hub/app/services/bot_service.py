from app.repositories.bot_repository import BotRepository

""" 
    Serviço responsável por gerenciar operações relacionadas a bots.
    Ele atua como uma camada entre os controladores da API e o repositório de bots.
 """
class BotService:

    # Registra um novo bot no sistema
    @staticmethod
    def register(
        db,
        bot_data
    ):

        return BotRepository.create(
            db,
            bot_data
        )

    # Lista todos os bots registrados no sistema
    @staticmethod
    def list_all(db):

        return BotRepository.get_all(db)

    # Atualiza o heartbeat de um bot específico
    @staticmethod
    def heartbeat(
        db,
        bot_id: int
    ):

        return BotRepository.update_heartbeat(
            db,
            bot_id
        )
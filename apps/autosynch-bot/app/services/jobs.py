import requests

""" 
    Serviço responsável por gerenciar operações relacionadas a jobs.
    Ele atua como uma camada entre o bot AutoSynch e o hub.
 """

# Classe que representa o serviço de jobs do bot AutoSynch
class JobService:

    HUB_URL = "http://127.0.0.1:8000"

    # Obtém a lista de jobs de um bot específico
    @classmethod
    def get_jobs(cls, bot_id: int):
        response = requests.get(
            f"{cls.HUB_URL}/api/v1/bots/{bot_id}/jobs"
        )
        return response.json()
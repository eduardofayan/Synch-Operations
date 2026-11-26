import requests

""" 
Serviço responsável pelo envio de batimentos cardíacos (heartbeat) do bot AutoSynch para o hub.
"""

# Classe que representa o serviço de envio de batimentos cardíacos (heartbeat) do bot AutoSynch
class HeartbeatService:
    # Inicializa o serviço de heartbeat com a URL do hub
    HUB_URL = "http://127.0.0.1:8000"

    # Envia um batimento cardíaco (heartbeat) para o hub
    @classmethod
    def send(cls, bot_id: int):
        response = requests.post(
            f"{cls.HUB_URL}/api/v1/bots/{bot_id}/heartbeat"
        )
        response.raise_for_status()
        return response.json()
import socket
import requests

""" 
 Serviço responsável pelo registro do bot AutoSynch no hub.
 """

# Classe que representa o serviço de registro do bot AutoSynch
class RegistrationService:

    # Inicializa o serviço de registro com a URL do hub
    HUB_URL = "http://127.0.0.1:8000"

    # Registra o bot no hub e retorna a resposta do servidor
    @classmethod
    def register(cls):
        machine_name = socket.gethostname()

        existing = requests.get(
            f"{cls.HUB_URL}/api/v1/bots/machine/{machine_name}"
        )
        if existing.status_code == 200:

            data = existing.json()

            if data:
                return {
                    "id": data["id"],
                    "created": False,
                }

        response = requests.post(
            f"{cls.HUB_URL}/api/v1/bots/register",
            json={
                "name": "AUTOSYNCH-BOT",
                "machine_name": machine_name,
                "version": "1.0.0"
            }
        )

        return response.json()
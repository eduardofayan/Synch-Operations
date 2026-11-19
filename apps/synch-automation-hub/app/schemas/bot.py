from pydantic import BaseModel

# Schemas para registro e resposta de bots
class BotRegister(BaseModel):
    name: str
    machine_name: str
    version: str

# Schema para resposta de bots
class BotResponse(BaseModel):
    id: int
    status: str
# Primeiros Passos

## Pré-Requisitos

- Python 3.11+
- Git
- VS Code
- PostgreSQL (futuro)

---

## Clonar o Projeto

```bash
git clone https://github.com/eduardofayan/Synch-Operations.git

cd Synch-Operations
```

## Criar Ambiente Virtual

```bash
python -m venv .venv
```

## Ativar Ambiente

PowerShell

```bash
.\.venv\Scripts\Activate.ps1
```

## Instalar Dependências

```bash
pip install -r apps/synch-automation-hub/requirements.txt
```

---

## Executar Synch Automation Hub

```bash
cd apps/synch-automation-hub

uvicorn app.main:app --reload
```

Acesse:

http://127.0.0.1:8000

---

## Executar AutoSynch Bot

```bash
cd apps/autosynch-bot

python -m app.main
```

Saída esperada:

```text
AutoSynch Agent iniciado
Buscando trabalhos...
```
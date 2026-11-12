# Ambiente Local

## Criar VENV

```bash
python -m venv .venv
```

## Ativar

```bash
.\.venv\Scripts\Activate.ps1
```

## Atualizar Pip

```bash
python -m pip install --upgrade pip
```

## Instalar Dependências

Hub

```bash
pip install -r apps/synch-automation-hub/requirements.txt
```

Bot

```bash
pip install pywin32
```

---

## Teste do Hub

```bash
cd apps/synch-automation-hub

uvicorn app.main:app --reload
```

---

## Teste do Bot

```bash
cd apps/autosynch-bot

python -m app.main
```

---

## Estrutura Atual

```text
apps/

├── autosynch-bot
├── synch-automation-hub
└── synch-insight
```
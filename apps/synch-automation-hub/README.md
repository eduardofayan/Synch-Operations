# Synch Automation Hub

## Visão Geral

O Synch Automation Hub é o núcleo operacional da plataforma Synch Operations.

Responsável por:

- Gerenciamento de agentes
- Registro de bots
- Heartbeat
- Orquestração de automações
- Filas
- Agendamentos
- Execuções
- Logs
- Governança

O Hub NÃO executa automações.

A execução ocorre nos AutoSynch Bots instalados no ambiente do cliente.

---

## Arquitetura

```text
AutoSynch Bot
        ↓
Synch Automation Hub
        ↓
PostgreSQL
        ↓
Synch Insight
```

---

## Executar aplicação

```bash
uvicorn app.main:app --reload
```

Documentação:

```text
http://127.0.0.1:8000/docs
```

---

## Banco de Dados

PostgreSQL

Banco:

```text
synch_operations
```

Usuário:

```text
synch_app
```

---

## Alembic

Gerar Migration

```bash
alembic revision --autogenerate -m "nome_da_migration"
```

Aplicar Migration

```bash
alembic upgrade head
```

Ver Migration Atual

```bash
alembic current
```

Histórico

```bash
alembic history
```

Reverter Última Migration

```bash
alembic downgrade -1
```

Downgrade 
```bash
alembic downgrade base
```

---

## Estrutura

```text
app/
├── api/
├── schemas/
├── repositories/
├── services/
├── models/
├── database/
├── core/
└── main.py
```

---

## Fluxo dos Agents

1. Agent inicia.
2. Agent registra no Hub.
3. Hub retorna agent_id.
4. Agent envia heartbeat.
5. Hub atualiza status.
6. Agent recebe jobs.
7. Agent executa automações.
8. Agent reporta resultado.

---

## Principais Entidades

- Tenants
- Roles
- Users
- Agents
- Automations
- Schedules
- QueueItems
- Executions
- ExecutionLogs

---

## Roadmap

### Sprint Atual

- Agent Registration
- Heartbeat
- Agent Monitoring

### Próximas

- Queue Engine
- Execution Engine
- JWT
- RBAC
- Synch Insight
- Synch Updater
```
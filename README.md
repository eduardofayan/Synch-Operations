# Synch Operations

Plataforma de Operações Digitais que conecta Automação, Integração de Dados, Analytics e Inteligência Artificial em um único ecossistema.

---

## Visão Geral

O ecossistema Synch Operations é composto por três produtos principais:

### AutoSynch Bot

Motor de execução responsável por:

- Automações Python
- RPA
- ETL
- Integrações
- Processamento de arquivos
- Processamento de e-mails

Executado localmente no ambiente do cliente.

---

### Synch Automation Hub

Centro de comando operacional.

Responsável por:

- Cadastro de automações
- Agendamentos
- Filas
- Logs
- Monitoramento
- Governança

O Hub não executa automações.

---

### Synch Insight

Plataforma de inteligência operacional.

Responsável por:

- Dashboards
- Analytics
- KPIs
- Relatórios
- Assistente Inteligente

---

## Arquitetura

Cliente

↓

AutoSynch Bot

↓

Synch Automation Hub

↓

Data Platform

↓

Synch Insight

↓

AI Assistant

---

## Estrutura do Repositório

```text
apps/

├── autosynch-bot/
├── synch-automation-hub/
└── synch-insight/

packages/
docs/
deployment/
tests/
```

## Tecnologias

### Backend

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL

### Frontend

- React
- TypeScript

### Observabilidade

- Loguru
- Prometheus
- Grafana

### Inteligência Artificial

- OpenAI
- Azure OpenAI
- LangChain

---

## Status Atual

### Concluído

- Estrutura do monorepo
- Documentação inicial
- Primeiro serviço FastAPI
- Primeiro AutoSynch Worker

### Em Desenvolvimento

- PostgreSQL
- SQLAlchemy
- Gestão de Agentes
- API Hub ↔ Bot

---

## Roadmap

Consulte:

docs/roadmap/roadmap.md
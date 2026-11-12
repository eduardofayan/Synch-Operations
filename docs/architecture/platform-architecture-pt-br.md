# Arquitetura da Plataforma

Este documento representa a arquitetura alvo da plataforma Synch Operations.

A primeira versão deve validar essas decisões considerando as restrições de rede, segurança e operação dos clientes.

---

# Arquitetura de Domínio

| Domínio | Responsável por | Limites |
|----------|----------|----------|
| Identidade e Multiempresa | Empresas, usuários, perfis, identidades de serviços e políticas | O Hub controla administração e acesso às APIs. O Insight controla acesso aos dados. |
| Catálogo de Automações | Definições de automações, versões, parâmetros, aprovações | O Hub apenas registra e distribui automações aprovadas. |
| Orquestração | Agendamentos, solicitações, distribuição, tentativas e cancelamentos | Responsável pela criação e distribuição das execuções. |
| Execução | Agentes, capacidades, execuções e resultados | O AutoSynch Bot executa os processos localmente no ambiente do cliente. |
| Observabilidade e Governança | Eventos, logs, métricas, alertas e auditoria | Recebe eventos de execução preservando o contexto da operação. |
| Dados e Analytics | Coleta, preparação de dados, indicadores e relatórios | Disponibiliza datasets para o Synch Insight. |
| Conhecimento e IA | Base de conhecimento, políticas de consulta, conversas e modelos de IA | Utiliza apenas dados autorizados. |

---

# Relações Principais

Uma empresa possui:

- Usuários
- Agentes
- Automações
- Bases de dados

Uma automação possui:

- Versões
- Agendamentos

Cada execução possui:

- Uma ou mais tentativas
- Um agente responsável
- Eventos associados

Os dados gerados alimentam os indicadores e análises do Synch Insight.

---

# Arquitetura de Componentes

```text
Usuários
    │
    ▼

Synch Automation Hub
    │
    ├── Catálogo
    ├── Agendamentos
    ├── Filas
    ├── Governança
    ├── Auditoria
    │
    ▼

PostgreSQL
    │
    ▼

AutoSynch Bot
    │
    ├── Agente
    ├── Scheduler
    ├── Executor
    ├── Conectores
    │
    ▼

Sistemas do Cliente
ERP
Banco de Dados
Arquivos
E-mails
APIs

    │
    ▼

Plataforma de Dados

    │
    ▼

Synch Insight

    ├── Dashboards
    ├── Indicadores
    ├── Analytics
    ├── Relatórios
    └── Assistente IA
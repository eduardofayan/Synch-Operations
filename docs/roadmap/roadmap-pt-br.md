# Roadmap de Evolução

## MVP

Objetivo: Validar a comunicação entre Hub e Bot.

### AutoSynch Bot

- Cadastro de agentes
- Execução local
- Execução agendada
- Execução sob demanda
- Logs estruturados
- Controle de tentativas

### Synch Automation Hub

- Login
- Cadastro de automações
- Catálogo
- Agendamentos
- Filas
- Histórico
- Logs

### Synch Insight

- Dashboard operacional básico
- Indicadores de automações
- Status dos agentes

### Saída esperada

Uma empresa consegue:

- Instalar um agente
- Executar automações
- Acompanhar resultados
- Consultar indicadores

---

## Versão 1.0

Objetivo: Disponibilizar uma base comercial.

### AutoSynch Bot

- ETL
- Integrações
- RPA Controlado
- Assinatura de artefatos

### Synch Automation Hub

- Alertas
- Aprovação de automações
- Controle de versões
- Gestão de filas avançada
- Relatórios operacionais

### Synch Insight

- Dashboards executivos
- Dashboards operacionais
- Relatórios
- Analytics

---

## Versão 2.0

Objetivo: Inteligência operacional.

### Synch Insight

Implementação do:

### Synch AI Assistant

Funcionalidades:

- Consultas em linguagem natural
- Resumo executivo
- Consulta documental
- Base de conhecimento

Exemplos:

- Quais automações falharam hoje?
- Qual o volume expedido ontem?
- Gere um resumo operacional da semana.

---

## Enterprise

Objetivo: Escalabilidade corporativa.

### Funcionalidades

- Multiempresa
- Federação de identidade
- Alta disponibilidade
- Gestão de múltiplos agentes
- Disaster Recovery
- Auditoria avançada
- Compliance LGPD
- Governança avançada de dados

---

## Visão Final

```text
AutoSynch Bot
        ↓
Synch Automation Hub
        ↓
Data Platform
        ↓
Synch Insight
        ↓
Synch AI Assistant


## Roteiro de entrega

As fases representam marcos de capacidade, não datas ou promessas. Segurança, isolamento de *tenant* (inquilino), testes e documentação operacional são requisitos de aceitação em todas as fases.

## MVP: comprovação do ciclo de controle e execução

- Implementar autenticação e autorização de *tenants*/usuários, um catálogo de automações com versões aprovadas, registro de agentes e um *bot* hospedado em ambiente Windows.
- Implementar execuções sob demanda e agendadas, filas/concessões (*leases*) persistentes, status de execução, mecanismos básicos de nova tentativa (*retry*) e cancelamento, logs estruturados e eventos de auditoria.
- Entregar uma interface central (*Hub UI*) simplificada, um conjunto de dados operacionais curado, um painel de *insights* básico e uma integração representativa com uma fonte externa.
- Disponibilizar a implantação do *Hub/Insight* via contêineres, migrações de PostgreSQL, monitoramento, instruções de backup/restauração e um manual de procedimentos (*runbook*) para o projeto-piloto do cliente.

**Critério de conclusão:** o projeto-piloto deve permitir o registro de um agente, a aprovação de uma versão, a execução de tarefas (sob demanda ou agendadas), o monitoramento de resultados (sucesso/falha), a recuperação após a desconexão de um agente — sem causar a duplicação silenciosa de efeitos — e a visualização de KPIs isolados por *tenant*. É necessário realizar testes de contrato, autorização, recuperação, migração e restauração utilizando dados sintéticos. Antes do início do piloto, deve haver um alinhamento sobre os riscos remanescentes e a responsabilidade pelo suporte.

## Versão 1: base comercial funcional

- Expandir conectores e cargas de trabalho suportadas, incluindo RPA controlado e processos de ETL/ELT; formalizar fluxos de assinatura, aprovação e atualização de artefatos.
- Adicionar funções (*roles*), alertas, operações de fila, estatísticas de execução, controles de retenção, relatórios operacionais, APIs documentadas e processos de integração (*onboarding*) de clientes.
- Publicar conjuntos de dados governados (somente leitura) para Power BI e Superset; adicionar recursos de recuperação de conhecimento e um assistente com reconhecimento de permissões, incluindo adaptadores para provedores e avaliação de respostas a perguntas de exemplo.
- Implementar automação de implantação, documentar a compatibilidade com Windows e Linux, realizar testes de capacidade, exercícios de recuperação de desastres e definir procedimentos de suporte.

**Critério de conclusão:** clientes representativos devem ser capazes de operar e atualizar o sistema de forma independente; o isolamento de *tenants*, as permissões de BI, a segurança em IA, os objetivos de recuperação e o desempenho devem estar em conformidade com os critérios de aceitação acordados.

## Enterprise: escala e governança

- Adicionar federação de identidades corporativas, fluxos avançados de políticas e aprovações, exportação detalhada de auditoria, gestão de ciclo de vida e políticas de retenção configuráveis.
- Oferecer suporte a alta disponibilidade, opções de implantação/residência regional, gestão de um conjunto (*fleet*) de agentes, escalabilidade e recuperação de desastres validada, conforme os compromissos assumidos com o cliente. - Ampliar a linhagem de dados, a qualidade, a governança semântica, as integrações de análise (analytics), a avaliação de IA e os controles sobre provedores; introduzir modelos adicionais de isolamento, quando necessário.

**Critério de conclusão:** demonstrar o atendimento aos requisitos acordados de disponibilidade, recuperação, conformidade e isolamento por meio de exercícios operacionais e de uma avaliação de segurança independente.
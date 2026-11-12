# Technical vision

## Goal and boundaries

Build a modular, multi-tenant control plane for automation and operational
intelligence, with customer-side execution that can operate behind corporate
firewalls. The Hub owns orchestration, not execution; agents execute only
approved, versioned workloads in the customer's environment. Insight consumes
governed data products rather than reaching directly into agent networks.

Start with a modular monolith for the Hub and separately deployable Bot and
Insight. Explicit module and API boundaries allow later extraction by scaling,
security, or operational need, not by default. Detailed contracts and
acceptance criteria are in the [platform architecture](platform-architecture.md)
and [roadmap](../roadmap/roadmap.md).

## Intended technology

| Concern | Target and role |
| --- | --- |
| Services and agent | Python 3.12; FastAPI for service APIs; SQLAlchemy and PostgreSQL for durable state |
| Web | React and TypeScript for Hub administration and Insight |
| Identity | External identity provider and short-lived JWTs; service and agent identities are distinct |
| Scheduling | APScheduler creates due work; durable database state, not the scheduler's memory, is authoritative |
| Packaging | Docker for server components; Windows service packaging for the Bot; Linux support where required |
| Observability | Structured Loguru logs, Prometheus metrics, Grafana dashboards and alerts |
| Analytics | Governed SQL views or exports for Power BI and Apache Superset |
| AI | Provider adapters for OpenAI and Azure OpenAI, with LangChain as an optional orchestration layer |

These are architectural targets, not implemented integrations. Choose supported
versions and assess dependencies and licenses when implementation begins.

## Quality attributes

- **Isolation:** tenant-scoped authorization and data access, tested at every
  boundary. Customer network access remains under customer control.
- **Reliability:** durable work records, leases, bounded retries, idempotent
  effects, reconciliation, and explicit partial failure states.
- **Security:** least privilege, encrypted transport, managed secrets,
  auditability, and controlled workload supply chain.
- **Operability:** correlation IDs, actionable metrics, backup and restore
  exercises, versioned configuration, and documented incident procedures.
- **Evolvability:** versioned contracts, backward-compatible migrations,
  independently deployable agents, and tested upgrade/rollback paths.
- **Data governance:** provenance, freshness, retention, access control, and
  human review for sensitive AI-assisted actions.

Availability objectives, recovery targets, capacity limits, tenancy deployment
model, supported agent versions, and data residency commitments must be agreed
with customers and measured before commercial production. Nothing in this
baseline constitutes a service-level agreement.

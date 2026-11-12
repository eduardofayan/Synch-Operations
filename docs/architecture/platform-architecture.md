# Platform architecture

This is a target design, not an implementation. The first release should
validate these decisions against customer network, security, and operational
constraints.

## Domain architecture

| Domain | Owns | Boundaries |
| --- | --- | --- |
| Identity and tenancy | Tenants, users, roles, service identities, policies | The Hub enforces administration and API access; Insight enforces data access. |
| Automation catalog | Automation definitions, versions, input schemas, approvals | Definitions reference approved artifacts; the Hub never runs them. |
| Orchestration | Schedules, run requests, dispatch, retry and cancellation policy | Creates durable runs and assigns eligible agents. |
| Execution | Agent registration, capabilities, execution attempts and results | Bot performs Python, RPA, ETL/ELT, email, file, and system work locally. |
| Observability and governance | Events, logs, metrics, alerts and audit records | Receives sanitized execution reports; preserves tenant and run context. |
| Data and analytics | Ingestion, curated datasets, KPI definitions, lineage and reports | Publishes governed read models for Insight and external BI. |
| Knowledge and AI | Knowledge sources, retrieval policies, conversations and model adapters | Uses authorized data only; responses are advisory unless separately approved. |

Core relationships: a tenant owns users, agents, automation definitions and
datasets; a definition has versions and schedules; each requested run has one
or more attempts, each leased to an eligible agent. Execution events and
artifacts reference tenant, run and attempt IDs. Analytics derives facts from
source events and business data, with provenance and freshness retained.

## Component architecture

```text
  Users / identity provider
        | HTTPS / JWT
        v
  Hub API + React UI ---------> Insight API + React UI
  catalog, scheduler, queue,     dashboards, reports, assistant
  agent control, audit           | governed datasets / retrieval
        |                       v
        +----------------> PostgreSQL + curated read models
        | outbound agent HTTPS         | read-only views / exports
        v                              v
  AutoSynch Bot                 Power BI / Apache Superset
  customer network                     |
  approved automation                 AI provider via governed adapter
        |
  local systems, files, email

  Hub / Insight / Bot -> sanitized logs and metrics -> monitoring pipeline
```

Arrows describe logical flows, not mandatory direct database access. Agents
initiate outbound TLS connections to the Hub; no inbound connection into the
customer network is required. The Bot authenticates as an enrolled, revocable
agent identity, advertises capabilities, polls for work, renews leases, and
uploads bounded, sanitized results. Separate enrollment credentials from user
JWTs; rotate credentials and validate identity, tenant, audience and expiry.
Customer policies determine network allowlists and local permissions.

FastAPI exposes versioned APIs for management and agent traffic. The Hub
persists queue records in PostgreSQL for the MVP; a broker can be introduced
later behind the dispatch contract. APScheduler triggers schedule evaluation,
but a single active scheduler or database-coordinated claims must prevent
duplicate creation across replicas. Store schedule timezone, DST policy and
misfire behavior explicitly; use a unique schedule/occurrence key so failover
and retries do not duplicate runs. On-demand requests also carry an
idempotency key scoped to the tenant and caller.

Runs move from `queued` to `leased`, `running`, and a terminal `succeeded`,
`failed`, or `cancelled` state. Each delivery creates an attempt with a lease
expiry and fencing token. Heartbeats renew valid leases; after expiry the Hub
reconciles and may retry according to policy. Reject stale agent updates and
deduplicate events by event ID. Delivery is at least once, not exactly once:
automation authors must make external side effects idempotent or reconcile
them before retrying. Cancellation is cooperative; report uncertain outcomes
when an agent disappears or an external action cannot be interrupted. Record
timeouts, retry limits, backoff, dead-letter review and operator decisions.

Artifacts must be approved and integrity-verified before execution. Constrain
agent identity, capabilities, local service account and filesystem access;
never permit arbitrary commands from untrusted users. The Hub records approvals
and deployment versions; the Bot enforces local execution policy.

## Data architecture

| Layer | Contents and owner | Controls |
| --- | --- | --- |
| Operational | PostgreSQL tenants, catalog, schedules, runs, attempts, audit metadata; Hub writes | Tenant-scoped keys and authorization, transactions, migrations, backup and restore. |
| Ingestion | Bot execution events and approved business-source extracts | Authenticated contracts, schema versions, event IDs, validation, provenance and replay policy. |
| Curated | Validated facts, dimensions and KPI definitions for Insight | Source/run lineage, timestamps, quality checks, tenant filters and refresh status. |
| Serving | Read-only views or tenant-scoped exports for Insight, Power BI and Superset | Least-privilege access, explicit dataset grants, row isolation, freshness metadata. |
| Artifacts and knowledge | Logs, reports, documents and AI retrieval indexes | Separate governed storage as needed, encryption, classification, retention and deletion policies. |

Keep operational and analytics workloads logically separate; choose physical
stores and pipelines based on volume and isolation requirements. PostgreSQL is
the initial durable store, not an assumption that all raw files or large
analytical workloads belong in it. BI tools connect only to approved, read-only
datasets or exports, never directly to operational write tables. Verify tenant
isolation for every access path, including BI credentials, exports and caches;
database row-level security can provide defense in depth, not replace
application authorization. Define ownership, data contracts, retention,
classification, residency and deletion for each dataset before ingestion.
Backups must be encrypted and restore-tested, including tenant recovery and
reconciliation with retained artifacts.

## AI and knowledge

An Insight request is authenticated and authorized before retrieval. Resolve
tenant and user permissions server-side, retrieve only approved documents or
curated data, and use a provider adapter with customer-approved OpenAI or Azure
OpenAI configuration. Natural-language data queries must target an allowlisted
semantic layer or constrained read-only query interface, enforce tenant and
row-level permissions, and apply limits/timeouts; never execute arbitrary
model-generated SQL against operational databases. Treat retrieved content and
model output as untrusted. Redact sensitive data, enforce egress and retention
policy, record access and model provenance without storing secrets, and show
sources and data freshness where possible. No autonomous write or execution
actions; future actions require explicit authorization and human approval.
Test prompt injection, cross-tenant access, hallucinations and provider failure.

## Deployment, security and operations

Deploy Hub and Insight as independently scalable Docker services with managed
PostgreSQL and TLS termination. Deploy the Bot as a least-privilege Windows
service in the client environment, with Linux support subject to compatible
workloads. Separate environments and secrets; no secrets in images, logs or
source. Automations requiring interactive desktop sessions need a documented
customer-approved session model, not an assumption that a Windows service can
interact with a desktop.

Loguru produces structured, redacted logs with tenant, run, attempt and
correlation IDs; avoid sensitive payloads and high-cardinality metric labels.
Prometheus collects service metrics and Grafana displays dashboards and alerts
for failed runs, queue age, expired leases, agent health and data freshness.
Agent metrics may need an outbound collector because the agent is behind a
firewall. Audit administrative actions and access separately from diagnostic
logs. Define incident response, upgrade compatibility, capacity and recovery
objectives and exercise backup/restore and agent disconnection before launch.

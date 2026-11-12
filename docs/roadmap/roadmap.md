# Delivery roadmap

Phases are capability gates, not dates or promises. Security, tenant
isolation, tests and operational documentation are acceptance requirements in
every phase.

## MVP: prove the control and execution loop

- Build tenant/user authentication and authorization, an automation catalog
  with approved versions, agent enrollment and a Windows-hosted Bot.
- Implement on-demand and scheduled runs, durable queue/leases, run status,
  basic retry and cancellation, structured logs and audit events.
- Deliver a small Hub UI, a curated operational dataset, basic Insight
  dashboard and one representative source integration.
- Provide containerized Hub/Insight deployment, PostgreSQL migrations,
  monitoring, backup/restore instructions and a customer pilot runbook.

**Exit:** a pilot can register an agent, approve a version, run a job on demand
and on schedule, observe success/failure, recover from agent disconnection
without silently duplicating effects, and view tenant-isolated KPIs. Exercise
contract, authorization, recovery, migration and restore tests with synthetic
data. Agree remaining risks and support ownership before pilot use.

## Version 1: usable commercial foundation

- Expand connectors and supported workloads including controlled RPA and
  ETL/ELT; formalize artifact signing, approval and upgrade workflows.
- Add roles, alerting, queue operations, run statistics, retention controls,
  operational reports, documented APIs and customer onboarding.
- Publish governed read-only datasets for Power BI and Superset; add
  knowledge retrieval and a permission-aware assistant with provider adapters
  and evaluation for the example questions.
- Add deployment automation, documented Windows and Linux compatibility,
  capacity tests, disaster recovery exercises and support procedures.

**Exit:** representative customers can operate and upgrade independently;
tenant isolation, BI permissions, AI safety, recovery objectives and
performance are verified against agreed acceptance criteria.

## Enterprise: scale and governance

- Add enterprise identity federation, advanced policy and approval workflows,
  richer audit export, lifecycle management and configurable retention.
- Support high availability, regional deployment/residency options, fleet
  management, scaling and tested disaster recovery according to customer
  commitments.
- Expand data lineage, quality, semantic governance, analytics integrations,
  AI evaluation and provider controls; introduce additional isolation models
  where required.

**Exit:** demonstrate agreed availability, recovery, compliance and isolation
requirements through operational exercises and independent security review.

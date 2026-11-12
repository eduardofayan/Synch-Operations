# Product vision

## Mission

Connect automation, data integration, analytics and AI into a single digital
operations ecosystem for industrial operations, logistics and business
intelligence. Keep execution close to customer systems while offering a
governed control plane and a clear view of business outcomes.

## Users and needs

| User | Need | Product |
| --- | --- | --- |
| Automation developer | Package and diagnose reliable integrations and RPA | AutoSynch Bot and Hub |
| Operations manager | Schedule work, monitor exceptions and understand throughput | Hub and Insight |
| Analyst | Govern and analyze trusted operational KPIs | Insight and BI integrations |
| Executive | See trends, risks and concise summaries | Insight |
| IT/security administrator | Control identities, deployment, network access and audit | All products |

## Product boundaries

- **AutoSynch Bot:** customer-side execution of approved Python, RPA,
  ETL/ELT, email, file and system integration jobs; local collection and
  reporting of operational outcomes. Supports scheduled and on-demand work
  delivered by the Hub.
- **Synch Automation Hub:** catalog, scheduling, queues, monitoring, logs,
  alerts, statistics, governance and user management. It controls agents and
  never executes customer automations.
- **Synch Insight:** dashboards, BI, KPIs, operational and executive analytics,
  reports, knowledge base and a governed conversational assistant.

The assistant should answer questions such as “What was yesterday's production
volume?”, “Which orders are delayed?” and “Generate an executive summary for
this week.” Answers depend on authorized, curated data and should disclose
sources and freshness. AI-generated answers are not a substitute for operator
review and do not authorize actions.

## Outcomes and assumptions

Measure time to detect failed work, successful run rate, queue age, time to
produce trusted KPIs, and adoption by operators and analysts. Establish
baselines and targets with pilot customers rather than asserting benefits.
Validate connectivity restrictions, Windows/RPA requirements, source data
quality, data residency and customer willingness to operate an agent before
committing to commercial service levels.

Delivery is staged in the [roadmap](../roadmap/roadmap.md).

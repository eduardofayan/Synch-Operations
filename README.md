# Synch Operations

Synch Operations is a proposed digital operations platform connecting automation,
data integration, analytics, and AI for industrial operations and logistics.

| Product | Responsibility |
| --- | --- |
| AutoSynch Bot | Executes automation in the customer's environment and reports results. |
| Synch Automation Hub | Catalogs, schedules, dispatches, governs, and observes work; it does **not** execute customer automations. |
| Synch Insight | Presents operational analytics, reports, and a governed AI assistant. |

## Status

This repository contains the initial architecture and reserved directories, not
an implemented or production-ready platform. There are no runnable services,
install instructions, dependencies, or automated tests yet. The architecture
describes intended behavior and controls to implement and validate before a
production deployment.

## Repository layout

```text
synch-operations/
├── apps/
│   ├── autosynch-bot/           # Customer-side execution agent
│   ├── synch-automation-hub/    # Control plane and administration
│   └── synch-insight/           # Customer analytics and assistant
├── packages/
│   ├── connectors/              # Reusable, controlled system adapters
│   ├── shared/                  # Versioned contracts and common primitives
│   ├── database/                # Persistence models and migrations
│   ├── logging/                 # Structured logging conventions
│   ├── security/                # Identity, authorization, and secret interfaces
│   └── ai/                      # Governed model and retrieval adapters
├── docs/
│   ├── architecture/            # Architecture and technical vision
│   ├── product/                 # Product vision
│   ├── roadmap/                 # Delivery phases and exit criteria
│   └── diagrams/                # Future maintained diagrams
├── deployment/
│   ├── docker/                  # Future container definitions
│   ├── windows/                 # Future Windows agent deployment
│   └── linux/                   # Future Linux deployment
├── tests/                       # Future cross-product and contract tests
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

Empty directories are kept with `.gitkeep` files. Application-specific tests
should live with their applications; `tests/` is for integration, end-to-end,
and contract tests spanning boundaries.

## Architecture and delivery

- [Technical vision](docs/architecture/technical-vision.md)
- [Domain, component, data, and deployment architecture](docs/architecture/platform-architecture.md)
- [Product vision](docs/product/product-vision.md)
- [MVP, version 1, and enterprise roadmap](docs/roadmap/roadmap.md)
- [Contributing](CONTRIBUTING.md)

The target stack is Python 3.12, FastAPI, PostgreSQL, SQLAlchemy, JWT,
APScheduler, Docker, Prometheus, Grafana, Loguru, React and TypeScript, with
Power BI and Apache Superset integration and OpenAI/Azure OpenAI via a
governed LangChain-compatible AI layer. These are design choices, not installed
or operational components.

No license has yet been selected; see [LICENSE](LICENSE).

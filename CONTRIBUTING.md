# Contributing

This repository is currently an architecture baseline. Discuss substantial
product, security, or architecture decisions in an issue before implementation.
Keep changes focused and update the relevant vision, architecture, and roadmap
when boundaries or delivery assumptions change.

## Proposed implementation conventions

- Keep execution in AutoSynch Bot, orchestration in the Hub, and customer
  analytics in Insight. Shared packages must not depend on applications.
- Use Python 3.12 for backend and agent code and React/TypeScript for web
  interfaces. Version contracts between independently deployed components.
- Add unit tests beside implementation and cross-product contract and
  integration tests under `tests/`. Cover tenant isolation, authorization,
  failure recovery, and idempotency where applicable.
- Never commit credentials, customer data, or sensitive logs. Use a secret
  manager and synthetic test data; document any new configuration.
- Changes to APIs, schemas, or events must document compatibility, migrations,
  and rollback. Validate security and observability at trust boundaries.

## Validation

No build, lint, or test tooling is configured yet. Review documentation links
and examples manually until implementation introduces reproducible commands.
When adding tooling, document setup and targeted checks here, run the relevant
checks, and describe what was verified in the change.

No license has been selected; contributions do not imply an open-source license.

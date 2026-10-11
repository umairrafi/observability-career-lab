# ObserveStack — local observability capstone

Single `docker compose up` stack for the observability career lab:

| Service | Role |
|---------|------|
| otel-collector | Receives OTLP; exports to Jaeger + Prometheus |
| jaeger | Trace UI (X-Ray mental model in interviews) |
| prometheus | Metrics scrape |
| grafana | Dashboards (RED/USE weeks 6, 8) |
| loki | Log aggregation (optional week 1–2 queries) |
| mock-sentry | Sentry-compatible relay stub |
| mock-pagerduty | Webhook receiver for alert routing drills |
| wiremock | Gateway failure injection (week 7) |

## Quick start

```bash
cp .env.example .env
docker compose up -d
open http://localhost:16686   # Jaeger
open http://localhost:3000    # Grafana (admin / see .env)
```

## PayFlow / TaskFlow wiring (week 10)

Clone sibling repos or add git submodules — **do not merge monorepos**:

```bash
# Example layout on your machine
~/career-labs/payments-career-lab/capstone/payflow-platform
~/career-labs/devops-career-lab/capstone/taskflow-platform
```

Point OTLP export to `http://localhost:4318` (HTTP) or `4317` (gRPC).

## Design decisions

- **No real DSNs** — `MOCK_SENTRY_DSN` in `.env.example` only.
- **No employer hostnames** in diagrams or configs.
- SLO doc: [slo.md](slo.md) · Runbook sample: [runbooks/payment-webhook-lag.md](runbooks/payment-webhook-lag.md)

## Makefile targets

- `make up` / `make down` — compose lifecycle
- `make demo-incident` — stub script for week 10 interview demo

#!/usr/bin/env python3
"""Regenerate observability-career-lab scaffold. Safe to re-run (overwrites generated files)."""
from __future__ import annotations

import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent

WEEKS = [
    (1, "structured-logging", "Structured logging and correlation", "126"),
    (2, "cloudwatch", "CloudWatch logs, metrics, alarms", "127"),
    (3, "opentelemetry", "OpenTelemetry instrumentation", "128"),
    (4, "distributed-tracing", "Distributed tracing (Jaeger + X-Ray mental model)", "129"),
    (5, "sentry", "Sentry errors, releases, performance", "130"),
    (6, "apm-dashboards", "APM dashboards (Grafana RED/USE patterns)", "131"),
    (7, "payment-alerting", "Payment-path alerting", "132"),
    (8, "slos", "SLIs, SLOs, error budgets", "133"),
    (9, "oncall-runbooks", "On-call, runbooks, postmortems", "134"),
    (10, "capstone-observestack", "Capstone ObserveStack", "135"),
]

MIT_LICENSE = """\
MIT License

Copyright (c) 2026 Muhammad Umair Virk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

GITIGNORE = """\
.DS_Store
.env
*.log
__pycache__/
.venv/
node_modules/
.idea/
.vscode/
*.tar.gz
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def root_readme() -> str:
    rows = "\n".join(
        f"| {n} | {topic} | Step {step} | `weeks/week-{n:02d}-{slug}/` |"
        for n, slug, topic, step in WEEKS
    )
    return f"""\
# Observability Career Lab

**10-week public lab** — structured logging, CloudWatch-style ops, OpenTelemetry, traces, Sentry, Grafana RED dashboards, payment alerting, SLOs, on-call runbooks, and the **ObserveStack** capstone. Closes the gap between “packages in repo” and “debugged production outages from logs.”

## Who this is for

- Senior/staff engineers preparing for **L24 observability depth** interviews (UAE/GCC fintech context welcome).
- You already touched PayFlow webhooks (payments lab W6) and TaskFlow Docker (devops lab W1–3).
- You will **not** use employer keys, schemas, or proprietary gateway secrets — only `MOCK_*` lab placeholders.

## Prerequisites

| Prior lab | Minimum |
|-----------|---------|
| [payments-career-lab](https://github.com/umairrafi/payments-career-lab) | Steps 1–6 (PayFlow webhooks) |
| [devops-career-lab](https://github.com/umairrafi/devops-career-lab) | Steps 36–38 (TaskFlow + CI) recommended before tracker step 126 |

**Tracker:** Steps **126–135** in the career lab master plan. Optional substitute for devops **Step 116 (W11)** when this lab is complete.

## Capstone — ObserveStack

Local Compose stack: OTel Collector, Jaeger, Prometheus, Grafana, Loki, Sentry-compatible relay stub, PagerDuty webhook mock.

```bash
cd capstone/observe-stack
cp .env.example .env
docker compose up -d
make demo-incident   # stub — wire in week 10
```

Instrument **PayFlow** and **TaskFlow** via documented clone paths (git submodule or sibling folders — no monorepo merge).

## 10-week roadmap

| Week | Topic | Tracker step | Folder |
|------|-------|--------------|--------|
{rows}

## Weekly structure

```text
weeks/week-NN-topic/
├── README.md
├── 01-lessons/
├── 02-hands-on/
├── 03-exercises/
└── 04-lab/
```

## Phase timing (per week)

| Phase | Days | Hours | Focus |
|-------|------|-------|-------|
| Lessons | 1–2 | 4–6 | Concepts + interview callouts |
| Hands-on | 3–4 | 4–6 | Runnable examples |
| Exercises | 5–6 | 3–5 | Try first, then solutions |
| Lab / capstone tie-in | 7 | 4–6 | PayFlow / TaskFlow / ObserveStack |

## Getting started

```bash
cd weeks/week-01-structured-logging
# Read README.md — week 1 is fully populated
docker --version
python3 --version
```

## Git workflow

- Branch per day optional: `week-01/day-2-hands-on`
- Commit prefix: `week-01: complete lesson 02 correlation ids`

## Progress tracking

- Per-week checklists in each `weeks/week-NN-*/README.md`
- Long-form notes: [`docs/learning-journey.md`](docs/learning-journey.md)

## Current week

Start here: [`weeks/week-01-structured-logging/README.md`](weeks/week-01-structured-logging/README.md)

---

**Muhammad Umair Virk** · Senior Software Engineer · UAE/GCC fintech · [engineering profile](https://github.com/umairvirk/engineering-profile)
"""


def learning_journey() -> str:
    blocks = []
    for n, slug, topic, _ in WEEKS:
        blocks.append(
            f"""\
## Week {n} — {topic}

**Dates:** ___________ to ___________

### Goals
- [ ] Complete lessons
- [ ] Finish hands-on examples
- [ ] Attempt exercises without solutions
- [ ] Lab milestone documented

### Notes & Aha Moments


### Interview Talking Points


### Questions for Tutor

"""
        )
    return "# Learning journey\n\nLog weekly progress for the observability career lab.\n\n" + "\n".join(blocks)


def week_readme_full() -> str:
    return """\
# Week 1: Structured logging and correlation — JSON logs across PayFlow and TaskFlow

**Duration:** 7 days (15–20 hours)  
**Outcome:** Parseable JSON logs with shared `trace_id` / `correlation_id` on stdout; grep across two containers; interview-ready explanation of cross-service correlation.

## What you'll know

- "Why one ID across webhook and API?"
- "When is `console.log` enough?"
- "Did you add structured logging in prod?" → packages present; **you** close gap #2 in lab first.

## Weekly schedule

| Day | Focus | Folder | Time |
|-----|-------|--------|------|
| 1 | Intro + log levels | `01-lessons/` | 2h |
| 2 | Correlation middleware | `01-lessons/` | 2h |
| 3 | JSON logging hands-on | `02-hands-on/` | 3h |
| 4 | Multi-container grep | `02-hands-on/` | 3h |
| 5 | Exercises | `03-exercises/` | 3h |
| 6 | Exercises + solutions review | `03-exercises/` | 2h |
| 7 | Week lab | `04-lab/` | 4h |

## Course structure

### Part 1 — Lessons

| # | File | Topic |
|---|------|-------|
| 1 | [01-intro.md](01-lessons/01-intro.md) | Why structured logging |
| 2 | [02-correlation-ids.md](01-lessons/02-correlation-ids.md) | trace_id / correlation_id |
| 3 | [03-production-patterns.md](01-lessons/03-production-patterns.md) | Middleware (.NET + Python sample) |

### Part 2 — Hands-on

| # | Example | Goal |
|---|---------|------|
| 1 | [example-01-plain-to-json](02-hands-on/example-01-plain-to-json/README.md) | Plain text → JSON |
| 2 | [example-02-correlation-grep](02-hands-on/example-02-correlation-grep/README.md) | Grep across two containers |

### Part 3 — Exercises

See [03-exercises/README.md](03-exercises/README.md). **Attempt without solutions first.**

### Part 4 — Lab

Extend PayFlow + TaskFlow log output — [04-lab/README.md](04-lab/README.md).

## Prerequisites

```bash
docker compose version
python3 --version
# Optional: dotnet --version for PayFlow samples
```

## How to study each lesson

Read → run → break → explain aloud → note questions → commit (`week-01: ...`).

## Progress checklist

- [ ] Lesson 01 intro
- [ ] Lesson 02 correlation ids
- [ ] Lesson 03 production patterns
- [ ] Hands-on example 01
- [ ] Hands-on example 02
- [ ] Exercises (no peeking at solutions)
- [ ] Week lab README complete

## Interview questions answered

- Structured vs unstructured logs on payment webhooks
- Propagating correlation ID from HTTP request to async handler
- Log query examples you would run in CloudWatch Logs Insights (preview week 2)

## Public writing (optional)

LinkedIn angle: "Closed observability gap #2 — structured logs with correlation IDs on PayFlow webhook path."
"""


def week_readme_stub(n: int, slug: str, topic: str, step: str) -> str:
    return f"""\
# Week {n}: {topic}

**Status:** Scaffold — content coming soon.  
**Tracker step:** {step}  
**Capstone touchpoint:** See [career-lab-ecosystem-extensions](https://github.com/umairvirk/engineering-profile/blob/main/docs/career-lab-ecosystem-extensions.md) (or local clone).

## Planned outcomes

Populate this week using the [career lab template](https://github.com/umairvirk/engineering-profile/blob/main/docs/career-lab-template.md):

- `01-lessons/` — deep dive + `> **Interview:**` callouts
- `02-hands-on/` — small runnable examples
- `03-exercises/` — starter + `solutions/`
- `04-lab/` — tie-in to PayFlow, TaskFlow, or ObserveStack

## Getting started (stub)

```bash
cd weeks/week-{n:02d}-{slug}
ls -la
```

## Progress checklist

- [ ] Lessons drafted
- [ ] At least one hands-on example
- [ ] Exercises README
- [ ] Lab milestone documented
"""


def lesson_intro() -> str:
    return """\
# Lesson 1 — Why structured logging

## Plain text is fine until it isn't

During local development, `console.log("paid")` is enough. In production you need **fields** you can filter: `level`, `service`, `trace_id`, `order_id`, `duration_ms`.

> **Production mistake:** Logging full card numbers or PII in JSON "because it's structured."

> **Interview:** "How did you find PR #214?" → CloudWatch filter on exception type + correlation id (week 2); reproduce locally with structured logs first.

## Three signals preview

| Signal | Week | Lab tool |
|--------|------|----------|
| Logs | 1 | stdout JSON |
| Metrics | 2, 6 | Prometheus / CW-style |
| Traces | 3–4 | OTel → Jaeger |

## PayFlow / TaskFlow touchpoints

- PayFlow: webhook handler and `/pay` API — emit `correlation_id` from incoming header or generate at edge.
- TaskFlow: API gateway middleware — same field name across stacks.

## Exercise for this lesson

List five fields you would require on every log line for a payment API. Explain each in one sentence.
"""


def lesson_correlation() -> str:
    return """\
# Lesson 2 — trace_id and correlation_id

## One ID across sync and async

Payment flows split: HTTP authorize → async webhook confirm. Without a shared ID, you cannot tie log lines across services.

**Convention for this lab:**

- `correlation_id` — business/request identifier (may come from client `X-Correlation-Id`)
- `trace_id` — W3C trace context (week 3–4); for week 1, use the same UUID if trace SDK not wired yet

> **Interview:** "Why one ID across webhook and API?" → Support and incident response; idempotent replay debugging; SLO burn investigation.

## Middleware pattern

1. Read incoming header or generate UUID at request start.
2. Store in `AsyncLocal` / request scope (.NET) or context var (Python).
3. Include in every log line via logger enricher.
4. Forward header on outbound HttpClient calls (preview week 4).

## Defensive Q&A

"Did you add structured logging in prod?" — cite packages in engineering profile §21.3; authorship unverified — **this lab proves you can wire it.**

## Break-it drill

Remove the enricher and trigger a webhook — show how grep fails without correlation.
"""


def lesson_production() -> str:
    return """\
# Lesson 3 — Production patterns (.NET + Python)

## Log levels

| Level | Use |
|-------|-----|
| Debug | Local only; sampling in prod |
| Info | Happy path milestones |
| Warning | Retryable failures |
| Error | User-visible or data inconsistency |

## .NET (conceptual)

Use `ILogger<T>` with structured templates:

```csharp
_logger.LogInformation("Payment authorized {OrderId} in {DurationMs}ms", orderId, sw.ElapsedMilliseconds);
```

Add middleware that sets `CorrelationId` on `HttpContext.Items` and a logging scope.

## Python (FastAPI sample)

```python
import logging, uuid
logger = logging.getLogger(__name__)

async def correlation_middleware(request, call_next):
    cid = request.headers.get("x-correlation-id") or str(uuid.uuid4())
    # bind cid to logging context (structlog or logging.Filter)
    response = await call_next(request)
    response.headers["x-correlation-id"] = cid
    return response
```

## Capstone milestone (week 1)

PayFlow + TaskFlow emit parseable JSON to stdout; README documents example `jq` / Logs Insights queries.

> **Production mistake:** Different field names per service (`reqId` vs `correlationId`) — breaks cross-service search.
"""


def observe_stack_readme() -> str:
    return """\
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
"""


def docker_compose() -> str:
    return """\
services:
  otel-collector:
    image: otel/opentelemetry-collector-contrib:0.96.0
    command: ["--config=/etc/otel-collector-config.yaml"]
    volumes:
      - ./config/otel-collector-config.yaml:/etc/otel-collector-config.yaml:ro
    ports:
      - "4317:4317"
      - "4318:4318"
      - "8888:8888"
    depends_on:
      - jaeger
      - prometheus

  jaeger:
    image: jaegertracing/all-in-one:1.54
    environment:
      COLLECTOR_OTLP_ENABLED: "true"
    ports:
      - "16686:16686"
      - "14268:14268"

  prometheus:
    image: prom/prometheus:v2.49.1
    volumes:
      - ./config/prometheus.yml:/etc/prometheus/prometheus.yml:ro
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana:10.3.1
    environment:
      GF_SECURITY_ADMIN_USER: admin
      GF_SECURITY_ADMIN_PASSWORD: ${GRAFANA_ADMIN_PASSWORD:-observestack}
    ports:
      - "3000:3000"
    depends_on:
      - prometheus
      - loki

  loki:
    image: grafana/loki:2.9.4
    command: -config.file=/etc/loki/local-config.yaml
    ports:
      - "3100:3100"

  mock-sentry:
    build: ./mocks/sentry
    environment:
      MOCK_SENTRY_DSN: ${MOCK_SENTRY_DSN:-http://mock-key@localhost:9999/1}
    ports:
      - "9999:8080"

  mock-pagerduty:
    build: ./mocks/pagerduty
    ports:
      - "9998:8080"

  wiremock:
    image: wiremock/wiremock:3.3.1
    ports:
      - "8089:8080"
    volumes:
      - ./mocks/wiremock:/home/wiremock
"""


def env_example() -> str:
    return """\
# ObserveStack — lab placeholders only. Never commit real DSNs or PD routing keys.

MOCK_SENTRY_DSN=http://mock-key@mock-sentry:8080/1
MOCK_PAGERDUTY_WEBHOOK=http://mock-pagerduty:8080/events
GRAFANA_ADMIN_PASSWORD=observestack
OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318
"""


def otel_config() -> str:
    return """\
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:

exporters:
  logging:
    loglevel: info
  otlp/jaeger:
    endpoint: jaeger:4317
    tls:
      insecure: true
  prometheus:
    endpoint: "0.0.0.0:8889"

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [logging, otlp/jaeger]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [logging, prometheus]
"""


def prometheus_config() -> str:
    return """\
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: otel-collector
    static_configs:
      - targets: ["otel-collector:8889"]
"""


def makefile() -> str:
    return """\
.PHONY: up down demo-incident logs

up:
\tdocker compose up -d

down:
\tdocker compose down

logs:
\tdocker compose logs -f --tail=100

demo-incident:
\t@echo "Week 10: wire PayFlow failure injection + trace/log correlation demo here."
\t@echo "Jaeger: http://localhost:16686  Grafana: http://localhost:3000"
"""


def slo_md() -> str:
    return """\
# ObserveStack SLOs (Week 8 template)

Map engineering profile §21.4 metrics to SLIs. Fill targets during week 8.

| SLI | Source | Lab measurement |
|-----|--------|-----------------|
| Checkout success rate | PayFlow metrics | Prometheus / Grafana |
| p95 authorize latency | PayFlow spans | Jaeger + RED dashboard |
| Webhook processing lag | PayFlow queue/logs | Loki / log query |
| TaskFlow availability | HTTP probe | Prometheus blackbox (optional) |
| Error budget policy | — | Document burn alerts in Grafana |

## Error budget policy (draft)

- **SLO target:** 99.5% checkout success over 30d
- **Alert:** Multi-window burn — page when 2h burn exceeds 14.4x budget (lab mock → PagerDuty stub)
"""


def runbook() -> str:
    return """\
# Runbook: Payment webhook lag

**Symptom:** Orders stuck in `authorized`; webhook consumer lag increasing.

## Detection

- Alert: `payflow_webhook_lag_seconds` > 300 (week 7)
- Logs: grep `correlation_id` across API + consumer (week 1)

## Mitigation

1. Confirm mock gateway / WireMock health (`curl localhost:8089/__admin/health`).
2. Scale consumer (TaskFlow pattern) or restart stuck worker container.
3. Replay webhooks from dead-letter with idempotency keys (payments lab W6).

## Escalation

- Route to on-call via `MOCK_PAGERDUTY_WEBHOOK` (week 9 tabletop).

## Post-incident

- Blameless postmortem template in week 9 exercises.
"""


def mock_sentry_dockerfile() -> str:
    return """\
FROM python:3.12-slim
WORKDIR /app
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
"""


def mock_sentry_app() -> str:
    return '''\
"""Minimal Sentry relay stub — accepts envelope POSTs for lab week 5."""
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        _ = self.rfile.read(length)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"id":"mock-event"}')

    def log_message(self, fmt, *args):
        print(f"[mock-sentry] {args[0]}")


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
'''


def mock_pd_app() -> str:
    return '''\
"""PagerDuty Events API v2 stub — logs incoming alerts for week 7/9."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        try:
            payload = json.loads(body)
            print("[mock-pagerduty]", json.dumps(payload, indent=2)[:500])
        except json.JSONDecodeError:
            print("[mock-pagerduty] invalid json")
        self.send_response(202)
        self.end_headers()
        self.wfile.write(b'{"status":"accepted"}')

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
'''


def stub_week_tree(week_dir: Path, n: int) -> None:
    write(week_dir / "01-lessons" / ".gitkeep", "")
    write(week_dir / "02-hands-on" / ".gitkeep", "")
    write(week_dir / "03-exercises" / "README.md", f"# Week {n} exercises\n\nComing soon.\n")
    write(week_dir / "03-exercises" / "solutions" / ".gitkeep", "")
    write(week_dir / "04-lab" / "README.md", f"# Week {n} lab\n\nComing soon.\n")


def week01_tree(week_dir: Path) -> None:
    write(week_dir / "01-lessons" / "01-intro.md", lesson_intro())
    write(week_dir / "01-lessons" / "02-correlation-ids.md", lesson_correlation())
    write(week_dir / "01-lessons" / "03-production-patterns.md", lesson_production())
    write(
        week_dir / "02-hands-on" / "example-01-plain-to-json" / "README.md",
        """\
# Example 01 — Plain text to JSON

## Goal

Emit one log line as JSON with `level`, `service`, `message`, `timestamp`.

## Steps

1. Run the sample script (add your own — `.NET` or `python3`).
2. Pipe stdout through `jq .`
3. Break: remove a required field and note query impact.

## Expected output

```json
{"level":"info","service":"payflow-lab","message":"webhook received","correlation_id":"..."}
```
""",
    )
    write(
        week_dir / "02-hands-on" / "example-02-correlation-grep" / "README.md",
        """\
# Example 02 — Grep across two containers

## Goal

Same `correlation_id` appears in API container logs and webhook worker logs.

## Steps

1. `docker compose up` two minimal services (or use ObserveStack + sample apps in week 10).
2. Send request with `X-Correlation-Id: lab-demo-1`.
3. `docker compose logs | grep lab-demo-1`

## What to break

Drop the header forwarding on HttpClient — traces/logs diverge.
""",
    )
    write(
        week_dir / "03-exercises" / "README.md",
        """\
# Week 1 exercises

Attempt without peeking at `solutions/` first.

| # | Exercise | Time |
|---|----------|------|
| 1 | Add JSON logger to a hello-world API | 45m |
| 2 | Middleware correlation id | 1h |
| 3 | Cross-container grep drill | 45m |
""",
    )
    write(week_dir / "03-exercises" / "solutions" / ".gitkeep", "")
    write(
        week_dir / "04-lab" / "README.md",
        """\
# Week 1 lab — PayFlow + TaskFlow structured logs

## Milestone

- PayFlow webhook + API emit JSON logs to stdout.
- TaskFlow gateway uses the same correlation field name.
- Document two example queries in this README (jq or Logs Insights syntax).

## Verify

```bash
# After wiring your clones
docker compose logs 2>&1 | jq -r 'select(.correlation_id!=null) | .correlation_id' | head
```
""",
    )


def week10_extra(week_dir: Path) -> None:
    write(
        week_dir / "04-lab" / "README.md",
        """\
# Week 10 lab — ObserveStack capstone

## Milestone

- `cd ../../capstone/observe-stack && docker compose up -d`
- Demo script: logs + trace + Sentry mock + metric for one failed order
- Record 5-minute interview walkthrough

## Commands

```bash
cd capstone/observe-stack
make up
make demo-incident
```
""",
    )


def generate() -> int:
    write(ROOT / "LICENSE", MIT_LICENSE)
    write(ROOT / ".gitignore", GITIGNORE)
    write(ROOT / "README.md", root_readme())
    write(ROOT / "docs" / "learning-journey.md", learning_journey())

    cap = ROOT / "capstone" / "observe-stack"
    write(cap / "README.md", observe_stack_readme())
    write(cap / "docker-compose.yml", docker_compose())
    write(cap / ".env.example", env_example())
    write(cap / "Makefile", makefile())
    write(cap / "slo.md", slo_md())
    write(cap / "config" / "otel-collector-config.yaml", otel_config())
    write(cap / "config" / "prometheus.yml", prometheus_config())
    write(cap / "runbooks" / "payment-webhook-lag.md", runbook())
    write(cap / "mocks" / "sentry" / "Dockerfile", mock_sentry_dockerfile())
    write(cap / "mocks" / "sentry" / "app.py", mock_sentry_app())
    write(cap / "mocks" / "pagerduty" / "Dockerfile", mock_sentry_dockerfile())
    write(cap / "mocks" / "pagerduty" / "app.py", mock_pd_app())
    write(cap / "mocks" / "wiremock" / "mappings" / ".gitkeep", "")

    for n, slug, topic, step in WEEKS:
        week_dir = ROOT / "weeks" / f"week-{n:02d}-{slug}"
        if n == 1:
            write(week_dir / "README.md", week_readme_full())
            week01_tree(week_dir)
        else:
            write(week_dir / "README.md", week_readme_stub(n, slug, topic, step))
            stub_week_tree(week_dir, n)
            if n == 10:
                week10_extra(week_dir)

    count = sum(1 for p in ROOT.rglob("*") if p.is_file() and p.name != "_generate_scaffold.py")
    print(f"Generated {count} files under {ROOT}")
    return count


if __name__ == "__main__":
    generate()

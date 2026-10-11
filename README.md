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
| 1 | Structured logging and correlation | Step 126 | `weeks/week-01-structured-logging/` |
| 2 | CloudWatch logs, metrics, alarms | Step 127 | `weeks/week-02-cloudwatch/` |
| 3 | OpenTelemetry instrumentation | Step 128 | `weeks/week-03-opentelemetry/` |
| 4 | Distributed tracing (Jaeger + X-Ray mental model) | Step 129 | `weeks/week-04-distributed-tracing/` |
| 5 | Sentry errors, releases, performance | Step 130 | `weeks/week-05-sentry/` |
| 6 | APM dashboards (Grafana RED/USE patterns) | Step 131 | `weeks/week-06-apm-dashboards/` |
| 7 | Payment-path alerting | Step 132 | `weeks/week-07-payment-alerting/` |
| 8 | SLIs, SLOs, error budgets | Step 133 | `weeks/week-08-slos/` |
| 9 | On-call, runbooks, postmortems | Step 134 | `weeks/week-09-oncall-runbooks/` |
| 10 | Capstone ObserveStack | Step 135 | `weeks/week-10-capstone-observestack/` |

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

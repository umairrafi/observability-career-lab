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

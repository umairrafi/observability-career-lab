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

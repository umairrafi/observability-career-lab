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

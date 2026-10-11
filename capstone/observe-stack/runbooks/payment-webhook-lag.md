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

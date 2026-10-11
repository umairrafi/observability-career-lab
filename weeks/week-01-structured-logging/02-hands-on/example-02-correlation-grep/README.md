# Example 02 — Grep across two containers

## Goal

Same `correlation_id` appears in API container logs and webhook worker logs.

## Steps

1. `docker compose up` two minimal services (or use ObserveStack + sample apps in week 10).
2. Send request with `X-Correlation-Id: lab-demo-1`.
3. `docker compose logs | grep lab-demo-1`

## What to break

Drop the header forwarding on HttpClient — traces/logs diverge.

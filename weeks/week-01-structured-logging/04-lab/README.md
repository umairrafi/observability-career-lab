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

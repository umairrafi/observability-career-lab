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

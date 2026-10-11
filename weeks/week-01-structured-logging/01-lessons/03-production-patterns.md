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

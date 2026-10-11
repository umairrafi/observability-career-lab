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

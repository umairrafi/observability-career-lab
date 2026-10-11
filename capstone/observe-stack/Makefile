.PHONY: up down demo-incident logs

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f --tail=100

demo-incident:
	@echo "Week 10: wire PayFlow failure injection + trace/log correlation demo here."
	@echo "Jaeger: http://localhost:16686  Grafana: http://localhost:3000"

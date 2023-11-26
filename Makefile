run: poetry_setup
	. .venv/bin/activate; \
		. scripts/run_hydra.sh;
.PHONY: run

poetry_setup: ## Setup virtual env and install dependencies
	$(MAKE) -f $(shell git rev-parse --show-toplevel)/.sca_repo_tooling_scripts/Makefile_sca_repo_shared $@
	poetry install --with dev --no-interaction -v
.PHONY: poetry_setup

compose-build:
	docker compose build

compose-up:
	docker compose up

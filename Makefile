.PHONY: install test pull push evaluate all help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	@pip install -r requirements.txt
	@cp .env.example .env

test: ## Run tests
	@pytest tests/ -v

pull: ## Pull prompts from LangSmith Hub
	@python src/pull_prompts.py

push: ## Push optimized prompts to LangSmith Hub
	@python src/push_prompts.py

evaluate: ## Run prompt evaluation
	@python src/evaluate.py

all: pull push evaluate ## Pull, push, and evaluate prompts

.PHONY: help install test lint format clean demo

help:
	@echo "Available commands:"
	@echo "  make install   - Install dependencies"
	@echo "  make test      - Run tests"
	@echo "  make lint      - Run linting"
	@echo "  make format    - Format code"
	@echo "  make demo      - Run demo"
	@echo "  make clean     - Clean cache files"

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/ -v

lint:
	ruff check purescout/
	black --check purescout/

format:
	black purescout/ tests/
	isort purescout/ tests/

demo:
	python main.py --mode demo

clean:
	rm -rf cache/
	rm -rf reports/
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	find . -name "*.pyc" -delete

lint:
	python -m py_compile scripts/*.py

test:
	python -m pytest tests/ -v

check: lint test

.PHONY: lint test check

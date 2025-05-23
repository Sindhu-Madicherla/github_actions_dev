.PHONY: test
test:
	@python3 -m coverage run -m pytest tests

.PHONY: coverage
coverage:
	@python3 -m coverage report > coverage.txt
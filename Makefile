.PHONY: test
test:
	@python3 -m pytest -p no:warnings -vv --cov=.

# .PHONY: coverage
# coverage:
# 	@python3 -m coverage report > coverage.txt


################
# .PHONY: test
# test:
# 	@python3 -m coverage run -m pytest model/v0/tests

# .PHONY: coverage
# coverage: ## run coverage
# 	@echo "Getting coverage report..."
# 	@python3 -m coverage report > coverage.txt

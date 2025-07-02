.PHONY: test
test:
	@python3 -m pytest tests -p no:warnings -vv --cov=.
	@python3 -m pytest tests_2 -p no:warnings -vv --cov=.

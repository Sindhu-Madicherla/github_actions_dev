.PHONY: test
test:
	@python3 -m pytest tests -p no:warnings -vv --cov=.

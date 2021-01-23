.PHONY: docs
docs:
	@sphinx-apidoc -f -o docs/source/ numerical_algorithms/
	@$(MAKE) -C docs clean
	@$(MAKE) -C docs html

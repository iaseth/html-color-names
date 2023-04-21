
default: readme

readme:
	python generate.py readme

css:
	python generate.py css

json:
	python generate.py json

html:
	python generate.py html

masterjson:
	python generate.py masterjson

clean:
	@rm -rf css
	@rm -rf json

.PHONY: readme css json

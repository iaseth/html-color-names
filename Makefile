
default: readme

readme:
	python generate.py readme

css:
	python generate.py css

json:
	python generate.py json

docs:
	python generate.py docs

png:
	python generate.py png

masterjson:
	python generate.py masterjson

mastercss:
	python generate.py mastercss


rmcss:
	rm -r css/*.css

rmjson:
	rm -r json/*.json

rmdocs:
	rm -r docs/*.html


clean:
	@rm -rf css
	@rm -rf json

.PHONY: readme css json png docs

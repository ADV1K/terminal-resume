build: data-file
	rm -rf advik/sections/
	poetry run python build.py resume.toml advik/sections
	poetry build

data-file: resume.toml
	curl -o resume.toml https://raw.githubusercontent.com/adv1k/adv1k/main/resume.toml

install: build
	poetry install

publish: build install
	poetry publish

.PHONY: build install publish data-file

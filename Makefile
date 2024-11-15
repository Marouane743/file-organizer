install:
	poetry install

build:
	poetry build

run:
	poetry run python file_organizer/main.py

test:
	poetry run pytest

clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info


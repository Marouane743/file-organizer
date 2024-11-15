install:
	poetry install

build:
	poetry build

run:
	poetry run python file_organizer/main.py $(DIR)

test:
	poetry run pytest

clean:
	rm -rf dist build *.egg-info



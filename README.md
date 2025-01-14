# File Organizer

**File Organizer** is a Python-based command-line tool designed to help you organize files within a specified directory by sorting them into folders based on file types (e.g., Images, Documents, Videos, Others). This project showcases the use of modern Python build tools and dependency management with **Poetry**, and automates build, testing, and execution processes with a **Makefile**.

This project is part of an assignment to demonstrate foundational skills in software development automation, including dependency management, packaging, and basic CLI functionality.

## Project Structure

```
file-organizer/
├── file_organizer/
│   ├── __init__.py         # Package initialization file
│   └── main.py             # Main code logic for organizing files
├── Makefile                # Makefile for automated commands
├── pyproject.toml          # Poetry configuration for dependencies and build settings
├── README.md               # Project documentation
└── tests/                  # Folder containing unit tests
    └── test_organizer.py   # Automated tests for the file organizer functionality
```

## Features

- **Automatic Organization**: Sorts files into categories such as Images, Documents, Videos, and Others based on file extensions.
- **Configurable**: Easily add more file types or categories by editing the configuration dictionary.
- **Command-Line Interface**: Simple to use with a CLI built using the `click` library.
- **Automated Build and Run**: Using Poetry and Makefile, the project is easy to install, run, and manage.

## Requirements

- **Python**: 3.8 or higher
- **Poetry**: For managing dependencies and builds ([Installation Guide](https://python-poetry.org/docs/#installation))

## Virtual Environment Setup

To ensure the project dependencies are isolated, create a virtual environment before proceeding.

1. **Create the Virtual Environment**:
   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   After activation, your terminal prompt will show `(venv)` to indicate the environment is active.

3. **Deactivate the Environment (When Done)**:
   To exit the virtual environment, run:
   ```bash
   deactivate
   ```

## Installation

Follow these steps to set up and run the File Organizer:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Marouane743/file-organizer.git
   cd file-organizer
   ```

2. **Set Up Dependencies Using Poetry**:
   Poetry will handle the virtual environment and install all necessary dependencies specified in `pyproject.toml`.
   ```bash
   poetry install
   ```

## Usage

Once installed, you can use the File Organizer from the command line to organize a specified directory.

### Basic Command

To organize files in a target directory, use:

```bash
poetry run python file_organizer/main.py <directory>
```

Replace `<directory>` with the path of the folder you want to organize. For example:

```bash
poetry run python file_organizer/main.py ~/Downloads
```

This will:
- Create folders for each category (Images, Documents, Videos, Others) within the specified directory if they don’t exist.
- Move files into these folders based on their extensions. Unsupported file types will go into the "Others" folder.

### Example

If you run:

```bash
poetry run python file_organizer/main.py ~/Documents
```

And if your **Documents** folder contains files like `photo.jpg`, `report.pdf`, and `movie.mp4`, they will be moved to **Images**, **Documents**, and **Videos** folders, respectively.

## Running Tests

To run the unit tests for the File Organizer project, use the following command:

```bash
poetry run pytest
```

Alternatively, you can use the `Makefile` command:

```bash
make test
```

The tests will automatically create temporary files, organize them, and check if they are moved to the correct folders.

## Build and Run with Makefile

For convenience, the project includes a **Makefile** with predefined commands to streamline common tasks. You can use the following commands:

- **Install Dependencies**: Installs all required dependencies via Poetry.
  ```bash
  make install
  ```

- **Build the Project**: Builds the package for distribution.
  ```bash
  make build
  ```

- **Run the Program**: Executes the File Organizer on the specified directory (update `Makefile` with your default directory or use the CLI command above for specific directories).
  ```bash
  make run
  ```

- **Run Tests**: Runs the unit tests to verify functionality.
  ```bash
  make test
  ```

- **Clean Up**: Deletes build artifacts to reset the environment.
  ```bash
  make clean
  ```

## Static Code Analysis

This project uses `flake8` for static code analysis.

### Installation
Install `flake8` with pip:
```bash
pip install flake8
```
## Pre-commit Hooks

This project uses `pre-commit` to automate static code analysis with `flake8`.

### Setup
1. Install `pre-commit`:
   ```bash
   pip install pre-commit


## Development

If you want to extend the functionality of this project, you can:

- **Add More File Types**: Open `file_organizer/main.py` and modify the `extensions` dictionary to include more file types. For example, you can add more video formats to the "Videos" category.

```python
extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],  # Added .avi as an example
    "Others": []
}
```

- **Add Tests**: Implement additional test cases in the `tests/` folder using `pytest` to test different scenarios.

## Documentation : 

To regenerate the documentation:
1. Install `pdoc`: `pip install pdoc`
2. Run: `pdoc file_organizer --output-dir docs/reference`
The generated documentation will be available in the `docs/reference` folder.


## Future Enhancements

This project is set up to be enhanced with the following features:
- **Automated Testing**: Additional `pytest` tests for comprehensive coverage.
- **Linting**: Set up `ruff` or `flake8` for code quality checks.
- **Documentation Generation**: Use Sphinx to generate technical documentation from docstrings.

\n## Documentation Deployment Test\n
\n## Documentation Deployment Test\n

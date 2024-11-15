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
└── README.md               # Project documentation
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

- **Run Tests**: (Future implementation) Will execute test cases if they are set up.
  ```bash
  make test
  ```

- **Clean Up**: Deletes build artifacts to reset the environment.
  ```bash
  make clean
  ```

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

- **Add Tests**: Implement test cases in a `tests/` folder using `pytest` for testing the CLI functionality and file organization logic.

## Future Enhancements

This project is set up to be enhanced with the following features:
- **Automated Testing**: Add `pytest` tests to ensure functionality.
- **Linting**: Set up `ruff` or other linting tools for code quality checks.
- **Documentation Generation**: Use Sphinx for generating technical documentation from docstrings.

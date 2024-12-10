# File Organizer Tutorial

This tutorial will guide you through setting up and using the **File Organizer** project effectively.

---

## Prerequisites

To use this project, ensure you have the following installed:
- Python **3.10 or higher**.
- **Poetry** for dependency management.

---

## Installation

### Step 1: Clone the Repository
Clone the project to your local system:
```bash
git clone https://github.com/Marouane743/file-organizer.git
cd file-organizer
```

### Step 2: Install Dependencies
Use `poetry` to install all required dependencies:
```bash
poetry install
```

---

## Usage

### Step 1: Prepare a Test Directory
Create a directory with some unorganized files:
```bash
mkdir test_directory
cd test_directory
touch photo.jpg report.pdf video.mp4 unknown.file
cd ..
```

### Step 2: Run the Organizer Script
Run the script to organize the files:
```bash
python file_organizer/main.py test_directory
```

---

## Features

- Automatically organizes files into categories:
  - **Images**: `.jpg`, `.png`, `.gif`, etc.
  - **Documents**: `.pdf`, `.txt`, `.docx`, etc.
  - **Videos**: `.mp4`, `.avi`, `.mkv`, etc.
  - **Others**: Files that don’t match any category.
- Handles duplicate files by appending a counter to their filenames (e.g., `photo_1.jpg`).

---

## Example

### Before Running the Script
```
test_directory/
├── photo.jpg
├── report.pdf
├── video.mp4
├── unknown.file
```

### After Running the Script
```
test_directory/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Videos/
│   └── video.mp4
├── Others/
│   └── unknown.file
```

---

## Debugging

Use the built-in logging system to troubleshoot any issues:
```bash
python file_organizer/main.py test_directory
```
Logs will display detailed insights about file movements and potential errors.

---

## Contribution

Contributions are welcome! Here’s how you can contribute:
1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for more details.




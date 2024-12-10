import os
from file_organizer.main import organize
from click.testing import CliRunner


def test_organize(tmp_path):
    # Set up a temporary directory with test files
    test_files = {
        "example.jpg": "fake image content",
        "example.pdf": "fake document content",
        "example.mp4": "fake video content",
        "example.txt": "fake text content",
    }

    for filename, content in test_files.items():
        file_path = tmp_path / filename
        file_path.write_text(content)

    # Use CliRunner to invoke the click command without pytest interference
    runner = CliRunner()
    result = runner.invoke(organize, [str(tmp_path)])

    # Check for successful execution
    assert result.exit_code == 0

    # Check that files have been moved to the correct folders
    assert os.path.exists(tmp_path / "Images" / "example.jpg")
    assert os.path.exists(tmp_path / "Documents" / "example.pdf")
    assert os.path.exists(tmp_path / "Videos" / "example.mp4")
    assert os.path.exists(
        tmp_path / "Documents" / "example.txt"
    )  # Text files are in Documents by default

    # Check that the temporary directory has the expected subdirectories
    for folder in ["Images", "Documents", "Videos", "Others"]:
        assert os.path.exists(tmp_path / folder)


def test_files_without_extensions(tmp_path):
    # Set up test files without extensions
    file_path = tmp_path / "no_extension"
    file_path.write_text("content")

    # Use CliRunner to invoke the organize command
    runner = CliRunner()
    result = runner.invoke(organize, [str(tmp_path)])

    # Check for successful execution
    assert result.exit_code == 0

    # Check that the file without an extension was moved to "Others"
    assert os.path.exists(tmp_path / "Others" / "no_extension")

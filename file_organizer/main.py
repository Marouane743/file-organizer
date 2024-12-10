import os
import shutil
import click


@click.command()
@click.argument("directory", type=click.Path(exists=True))
def organize(directory):
    """Organize files in the specified directory by file type."""
    extensions = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Others": [],
    }

    for folder, exts in extensions.items():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            moved = False
            for folder, exts in extensions.items():
                if any(file.lower().endswith(ext) for ext in exts):
                    shutil.move(file_path, os.path.join(directory, folder, file))
                    moved = True
                    break

            if not moved:
                shutil.move(file_path, os.path.join(directory, "Others", file))

    print(f"Files in '{directory}' have been organized.")


if __name__ == "__main__":
    organize()

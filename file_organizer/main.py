import logging
import os
import shutil
import click


logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# Function to resolve duplicate file names
def resolve_duplicate(destination):
    base, extension = os.path.splitext(destination)
    counter = 1
    while os.path.exists(destination):
        destination = f"{base}_{counter}{extension}"
        counter += 1
    return destination


@click.command()
@click.argument("directory", type=click.Path(exists=True))
def organize(directory):
    extensions = {
        "Images": [".jpg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Others": [],
    }

    logger.info(f"Starting to organize the directory: {directory}")
    try:
        if not os.path.exists(directory):
            logger.error(f"Directory does not exist: {directory}")
            return

        logger.debug("Creating folders for file types...")
        for folder in extensions.keys():
            folder_path = os.path.join(directory, folder)
            os.makedirs(folder_path, exist_ok=True)
            logger.debug(f"Created or verified folder: {folder_path}")

        logger.debug("Moving files to corresponding folders...")
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                moved = False
                for folder, exts in extensions.items():
                    if file.lower().endswith(tuple(exts)):
                        target_folder = os.path.join(directory, folder)
                        destination = os.path.join(target_folder, file)
                        destination = resolve_duplicate(
                            destination
                        )  # Handle duplicates
                        shutil.move(file_path, destination)
                        logger.info(f"Moved file {file} to {folder}")
                        moved = True
                        break
                if not moved:
                    target_folder = os.path.join(directory, "Others")
                    destination = os.path.join(target_folder, file)
                    destination = resolve_duplicate(destination)  # Handle duplicates
                    shutil.move(file_path, destination)
                    logger.warning(
                        f"File {file} moved to Others (no matching extension)"
                    )
        logger.info("Organization complete.")
    except Exception as e:
        logger.critical(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    organize()

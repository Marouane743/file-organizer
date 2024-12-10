import os

# Define the test directory and unorganized files
test_directory = "./test_directory"
unorganized_files = [
    "photo.jpg",
    "graphic.png",
    "drawing.gif",  # Image files
    "report.pdf",
    "essay.docx",
    "notes.txt",  # Document files
    "movie.mp4",
    "clip.avi",
    "animation.mkv",  # Video files
    "README.md",
    "script.sh",
    "config.yaml",  # Other types
    "randomfile.unknown",
    "weirdfile.data",
    "nofileextension",  # Unsorted
]

# Create the test directory and populate it with unorganized files
os.makedirs(test_directory, exist_ok=True)
for file in unorganized_files:
    file_path = os.path.join(test_directory, file)
    with open(file_path, "w") as f:
        f.write(f"Sample content for {file}")

import os
import shutil
from pathlib import Path

def organize_files(directory: Path):
    if not directory.is_dir():
        print(f"The path {directory} is not a valid directory.")
        return

    for item in directory.iterdir():
        if item.is_file():
            # Extract the file extension
            extension = item.suffix[1:]   # Remove the leading dot from the extension
            if extension:   # Only proceed if the file has an extension
                extension_folder = directory / extension

                # Create the folder for the extension if it doesn't exist
                if not extension_folder.exists():
                    extension_folder.mkdir()

                # Move the file to the appropriate folder
                shutil.move(str(item), str(extension_folder / item.name))

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to organize: ").strip()
    organize_files(Path(folder_path))

import os
from pathlib import Path

# default location; override via command-line argument
download_path = Path.home() / "Descargas"
DIRECTORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".csv"],
    "Archives": [".zip", ".tar", ".gz"],
    "Installers": [".deb", ".iso"],
}

def organize_junk(path: Path = download_path):
    """Move files from *path* into categorized subfolders based on extension.

    Parameters
    ----------
    path : pathlib.Path
        Directory to organize. Defaults to ``~/Descargas``.
    """

    if not path.exists():
        print(f"Directory does not exist: {path}")
        return

    for item in path.iterdir():
        if item.is_dir():
            continue
        file_extension = item.suffix.lower()
        for category, extensions in DIRECTORIES.items():
            if file_extension in extensions:
                target_folder = path / category
                target_folder.mkdir(exist_ok=True)
                item.rename(target_folder / item.name)
                print(f"Moved: {item.name} -> {category}")
    print(f"Done! Your {path.name} folder is clean.")


if __name__ == "__main__":
    organize_junk()
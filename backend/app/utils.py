import re
from pathlib import Path
import os

def sanitize_filename(name: str) -> str:
    """
    Removes invalid characters from filenames (Windows-safe).
    
    Args:
        name (str): Original filename.
    
    Returns:
        str: Sanitized filename.
    """
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def ensure_downloads_dir() -> str:
    """
    Ensures the 'downloads' directory exists.
    Returns the absolute path to the downloads directory.
    """
    download_dir = os.getenv("DOWNLOADS_DIR", "downloads")
    path = Path(download_dir)
    path.mkdir(exist_ok=True)
    return str(path.resolve())

def is_valid_url(url: str) -> bool:
    """
    Improved URL validation using regex.
    """
    regex = re.compile(
        r'^(?:http|https)://'  # http:// or https://
        r'(?:\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def get_unique_filename(directory: str, filename: str) -> str:
    """
    Returns a unique filename in the directory to avoid overwriting.
    """
    base, ext = os.path.splitext(filename)
    counter = 1
    unique_filename = filename
    while Path(directory, unique_filename).exists():
        unique_filename = f"{base}_{counter}{ext}"
        counter += 1
    return unique_filename

import subprocess
import sys
from pathlib import Path
from typing import Optional

from . import logger

def ensure_repopack_installed() -> None:
    """Ensure Repopack is installed globally."""
    try:
        subprocess.run(
            ["repopack", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.warning("Repopack not found. Installing globally...")
        try:
            subprocess.run(["npm", "install", "-g", "repopack"], check=True)
        except subprocess.CalledProcessError as e:
            logger.error("Failed to install Repopack. Please install it manually:")
            logger.console.print("npm install -g repopack")
            sys.exit(1)

def run_repopack(directory: Path, output_file: Path) -> None:
    """Run Repopack on a directory."""
    try:
        subprocess.run([
            "repopack",
            str(directory),
            "-o", str(output_file)
        ], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to run Repopack: {e}")
        sys.exit(1)

def read_file(path: Path) -> str:
    """Read and return the contents of a file."""
    try:
        return path.read_text(encoding='utf-8')
    except Exception as e:
        logger.error(f"Failed to read file {path}: {e}")
        sys.exit(1)

def write_file(path: Path, content: str) -> None:
    """Write content to a file."""
    try:
        path.write_text(content, encoding='utf-8')
    except Exception as e:
        logger.error(f"Failed to write file {path}: {e}")
        sys.exit(1)

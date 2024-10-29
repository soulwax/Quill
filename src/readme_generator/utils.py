import subprocess
import sys
from pathlib import Path
from typing import Optional

from . import logger

def run_repopack(directory: Path, output_file: Path) -> None:
    """Run Repopack on a directory using npx."""
    try:
        logger.debug("Packing codebase with Repopack...")  # Changed from info to debug
        subprocess.run([
            "npx",
            "repopack",
            str(directory),
            "-o", str(output_file)
        ], check=True)
        logger.success(f"Successfully packed codebase into {output_file}")  # Changed from info to success
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
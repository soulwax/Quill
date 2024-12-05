from pathlib import Path
from typing import Optional
import repopack

from . import logger

def run_repopack(directory: Path, output_file: Path) -> None:
    """Run Repopack on a directory using the Python package."""
    try:
        logger.debug("Packing codebase with Repopack...")
        # Create a Repopack instance and pack the directory
        packer = repopack.RepoPack(
            repo_path=str(directory),
            output_path=str(output_file),
            exclude_patterns=[],  # You can add patterns from .gitignore here if needed
            file_handlers={}  # Default handlers should work fine
        )
        packer.pack()
        logger.success(f"Successfully packed codebase into {output_file}")
    except Exception as e:
        logger.error(f"Failed to run Repopack: {e}")
        raise

def read_file(path: Path) -> str:
    """Read and return the contents of a file."""
    try:
        return path.read_text(encoding='utf-8')
    except Exception as e:
        logger.error(f"Failed to read file {path}: {e}")
        raise

def write_file(path: Path, content: str) -> None:
    """Write content to a file."""
    try:
        path.write_text(content, encoding='utf-8')
    except Exception as e:
        logger.error(f"Failed to write file {path}: {e}")
        raise
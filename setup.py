# File: setup.py

from setuptools import setup, find_packages

setup(
    name="quill",  # Changed from readme-generator-cli
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "google-generativeai>=0.2.0",
        "python-dotenv>=1.0.0",
        "rich>=13.7.0",
        "repopack>=0.1.4",  # Add this to match pyproject.toml
    ],
    entry_points={
        "console_scripts": [
            "quill=readme_generator.__main__:main",  # Update command name
        ],
    },
)
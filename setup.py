from setuptools import setup, find_packages

setup(
    name="readme-generator-cli",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "google-generativeai>=0.2.0",
        "python-dotenv>=1.0.0",
        "rich>=13.7.0",
    ],
    entry_points={
        "console_scripts": [
            "readme-generator=readme_generator.__main__:main",
        ],
    },
)
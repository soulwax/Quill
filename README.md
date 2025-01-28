# Quill: README Generator

Quill is a command-line tool that uses LLMs to generate comprehensive `README.md` files for your projects. The README you're reading right now was generated using Quill!

## Technologies Used

* **Python:** The primary programming language.
* **Google Gemini:** The large language model used for README generation.
* **Repopack:** For efficient codebase packaging.
* **Rich:** For enhanced console output and progress display.
* **Python-dotenv:** For loading environment variables from a `.env` file.

## Prerequisites

* **Python 3.9 or higher:** Ensure you have a compatible Python version installed.
* **Google Cloud Platform Project and Gemini API Key:** You need a GCP project and an active Gemini API key. Instructions on how to obtain one are available on the Google Cloud Platform documentation. See the Configuration section below for details on how to set this up.
* **pip:** Python's package installer.

## Installation

### Standard Installation

You can install Quill directly from PyPI:

```bash
pip install quill
```

### Development Installation

If you want to contribute or modify the code:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/usedispatch/Quill.git
   cd Quill
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux/macOS
   venv\Scripts\activate    # On Windows
   ```

3. **Install in development mode:**

   ```bash
   pip install -e .
   ```

## Configuration

Before using Quill, you need to set your Google Gemini API key. Create a `.env` file in your project directory and add your API key:

```plaintext
GEMINI_API_KEY=your_gemini_api_key
```

You can also optionally configure these environment variables for customization:

* `GEMINI_MODEL`: The Gemini model to use (default: `gemini-pro`).
* `DEFAULT_OUTPUT`: The default name for the Repopack output file (default: `repopack-output.txt`).
* `DEFAULT_README`: The default name for the generated README file (default: `README.md`).
* `GENERATION_TEMPERATURE`: Controls the randomness of the LLM's output (default: 0.7). A higher value (closer to 1.0) will result in more creative and unpredictable outputs; a lower value (closer to 0.0) will make the output more deterministic.
* `MAX_OUTPUT_TOKENS`: Limits the maximum number of tokens in the generated README (default: 8192).

## Usage

Quill is used via the command line. The basic usage is:

```bash
quill <directory> [-o <output_file>] [-r <readme_file>] [-k] [--temp-dir <temp_dir>] [--verbose]
```

* `<directory>`: The path to the directory containing your project's codebase (defaults to the current directory).
* `-o <output_file>`: Specifies the name of the Repopack output file (optional).
* `-r <readme_file>`: Specifies the name of the generated README file (optional).
* `-k`: Keeps the Repopack output file after generating the README (optional).
* `--temp-dir <temp_dir>`: Specifies a custom temporary directory (optional).
* `--verbose`: Enables verbose logging (optional).

**Example:**

To generate a README for the current directory, saving the Repopack output as `my_repo.txt` and the README as `MY_README.md`, run:

```bash
quill -o my_repo.txt -r MY_README.md
```

## Project Structure

```bash
Quill/
├── src/
│   └── quill/
│       ├── logger/
│       │   ├── __init__.py
│       │   └── logger.py
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── config.py
│       ├── generator.py
│       └── utils.py
├── tests/
│   └── conftest.py
├── LICENSE
├── pyproject.toml
├── requirements-dev.txt
├── requirements.txt
└── setup.py
```

* `src/`: Contains the source code for the Quill application.
* `tests/`: Contains unit tests for the project.
* `LICENSE`: The project's license file.
* `pyproject.toml`: Project metadata and build system configuration.
* `requirements.txt`: Project dependencies.
* `requirements-dev.txt`: Development dependencies.
* `setup.py`: Setup script for installing the package.

## Contributing Guidelines

(This section would be populated based on any contributing guidelines found within the codebase, but none were provided in the input.)

## License Information

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Error Messages

* **`ValueError: GEMINI_API_KEY not found in environment variables`:** This error occurs if the `GEMINI_API_KEY` environment variable is not set. Make sure you have configured your Gemini API key as described in the Configuration section.
* **`RuntimeError: Repopack CLI not found...`:** This indicates that Repopack is not installed. Install it using `pip install repopack`.
* **`RuntimeError: Repopack command failed...`:** This means there was an error running the Repopack command. Check the verbose logs for more details.
* **`RuntimeError: Failed to generate README...`:** This indicates a failure in the LLM generation process. Check the verbose logs for potential errors and retry. There could be issues with your Gemini API Key or network connectivity.
* **`FileNotFoundError: Directory not found...` or `FileNotFoundError: File not found...`:** Check if the specified directory or file exists.

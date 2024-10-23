# README Generator CLI

## Description

This CLI tool leverages Repopack and Google Gemini to automatically generate comprehensive README files for your projects. It analyzes your codebase, extracts relevant information, and generates a well-structured and informative README.md.

## Key Features

- **Automated README generation:** Saves you time and effort by generating README files with minimal manual intervention.
- **Comprehensive content:**  Includes project description, key features, technologies used, prerequisites, installation instructions, usage examples, configuration details, project structure, contributing guidelines, and licensing information.
- **Gemini integration:**  Uses Gemini's advanced language model to generate high-quality, human-like README content.
- **Repopack integration:** Efficiently packs your entire codebase into a single file for seamless analysis by Gemini.

## Technologies Used

- **Python:** The primary language for the CLI tool.
- **Repopack:** A tool for packing entire codebases into single files.
- **Gemini:** Google's powerful language model for natural language understanding and generation.
- **Rich:** Provides rich terminal output for user feedback and progress tracking.
- **Python-dotenv:** Enables loading configuration from environment variables.

## Prerequisites

- **Python 3.9 or later:**  Ensure Python is installed on your system.
- **Node.js:** Needed for installing Repopack globally.
- **API Key:** Obtain your own Google Gemini API key using Flash 1.5 for free from [here](https://ai.google.dev/gemini-api/docs/api-key).
- **Environment Variables:** You need to set the following environment variables:
    - `GEMINI_API_KEY`: Your Gemini API key.

## Installation

1. **Install Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Repopack globally:**
   ```bash
   npm install -g repopack
   ```

3. **Set environment variables:**
   - **Manually:** Create a `.env` file in your project root directory and add the following line, replacing `YOUR_GEMINI_API_KEY` with your actual key:
     ```
     GEMINI_API_KEY=YOUR_GEMINI_API_KEY
     ```
   - **In your shell:**  Set the environment variable directly in your terminal:
     ```bash
     export GEMINI_API_KEY=YOUR_GEMINI_API_KEY
     ```

## Usage

1. **Navigate to your project directory:**
   ```bash
   cd your_project_directory
   ```

2. **Run the CLI tool:**
   ```bash
   readme-generator
   ```

   **Optional arguments:**

   - `-o, --output`: Specify the output file name for the packed codebase (default: `repopack-output.txt`).
   - `-r, --readme`: Specify the output file name for the generated README (default: `README.md`).
   - `-k, --keep-packed`: Keep the packed codebase file after generation.
   - `--temp-dir`: Specify a custom temporary directory for processing.
   - `-v, --verbose`: Enable verbose output for debugging.

**Example:**
```bash
readme-generator -o my_project_code.txt -r readme.md -k
```

This command will:

- Process the current directory.
- Save the packed codebase to `my_project_code.txt`.
- Generate the README file as `readme.md`.
- Keep the `my_project_code.txt` file after generation.

## Project Structure

```
├── src
│   └── readme_generator
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── config.py
│       ├── generator.py
│       ├── logger.py
│       └── utils.py
└── tests
    └── conftest.py

```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear and concise commit messages.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Error Messages

**Common Error Messages:**

- **"GEMINI_API_KEY not found in environment variables"**: Make sure you have set the `GEMINI_API_KEY` environment variable correctly.
- **"Repopack not found. Installing globally..."**: If Repopack is not found, the script will attempt to install it globally. If the installation fails, you need to install it manually using `npm install -g repopack`.
- **"Failed to run Repopack: ..."**:  Check that you have Repopack installed correctly and that your project directory is valid.
- **"Failed to generate README: ..."**:  This could indicate a problem with your Gemini API key or a network connection issue.

**Additional Information:**

- **Repopack Documentation:** [https://github.com/yamadashy/repopack](https://github.com/yamadashy/repopack)
- **Gemini Documentation:** [https://cloud.google.com/generative-ai](https://cloud.google.com/generative-ai)


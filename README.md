## README Generator CLI

A command-line tool that automatically generates comprehensive README.md files for your projects using an LLM. This README was generated via the tool! 

### Prerequisites

- Python 3.9 or later
- Node.js and npm (for package dependencies)
- Google Cloud Platform (GCP) account and a Gemini API Key
    - Get your free Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Installation

1. **Install Node.js and Python if needed:**
   - Install Python from [python.org](https://www.python.org/)
   - Install Node.js from [nodejs.org](https://nodejs.org/)

2. **Clone the repository:**
   ```bash
   git clone https://github.com/mainnebula/ReadMe-Generator
   cd ReadMe-Generator
   ```

3. **Create and activate a virtual environment:**
   ```bash
   # Create virtual environment
   python -m venv .venv

   # Activate it
   # On Unix/MacOS:
   source .venv/bin/activate
   # On Windows:
   # .venv\Scripts\activate
   ```

4. **Install in development mode:**
   ```bash
   # This will install both Python and Node.js dependencies
   pip install -e .
   ```

### Usage Tutorial

#### 1. Basic Usage (Same Directory)

```bash
# Activate the virtual environment if not already active
source /path/to/ReadMe-Generator/.venv/bin/activate

# Create .env file with your API key
echo "GEMINI_API_KEY=your_key_here" > .env

# Generate README for the current directory
readme-generator
```

#### 2. Using in Other Directories

There are two ways to use the tool in different directories:

**Method A: With Activated Virtual Environment**
```bash
# 1. Activate the virtual environment
source /path/to/ReadMe-Generator/.venv/bin/activate

# 2. Navigate to your project
cd /path/to/your/project

# 3. Create .env file
echo "GEMINI_API_KEY=your_key_here" > .env

# 4. Generate README
readme-generator
```

**Method B: Using Full Path (No Activation Required)**
```bash
# 1. Navigate to your project
cd /path/to/your/project

# 2. Create .env file
echo "GEMINI_API_KEY=your_key_here" > .env

# 3. Run using full path
/path/to/ReadMe-Generator/.venv/bin/readme-generator
```


#### 3. Command Options

```bash
# Show help
readme-generator --help

# Generate with verbose output
readme-generator --verbose

# Custom output files
readme-generator -o custom-output.txt -r CUSTOM-README.md

# Keep the intermediate file
readme-generator -k

# Process a specific directory
readme-generator /path/to/directory

# Combine options
readme-generator --verbose -k -o packed.txt -r docs/README.md /path/to/directory
```

### Common Use Cases

1. **Generate README for a sibling project:**
   ```bash
   cd ../another-project
   /path/to/ReadMe-Generator/.venv/bin/readme-generator
   ```

2. **Generate README for a project in your home directory:**
   ```bash
   /path/to/ReadMe-Generator/.venv/bin/readme-generator ~/projects/my-app
   ```
   
3. **Generate README with detailed logging:**
   ```bash
   readme-generator --verbose
   ```

4. **Generate README in a custom location:**
   ```bash
   readme-generator -r docs/PROJECT-README.md
   ```

### Configuration

The tool reads these environment variables (in your .env file):

- `GEMINI_API_KEY` (required): Your Gemini API key
- `GEMINI_MODEL` (optional): The model to use (default: gemini-1.5-flash)
- `DEFAULT_OUTPUT` (optional): Default output filename (default: repopack-output.txt)
- `DEFAULT_README` (optional): Default README filename (default: README.md)

### Project Structure

```
ReadMe-Generator/
├── src/
│   └── readme_generator/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── config.py
│       ├── generator.py
│       ├── logger.py
│       └── utils.py
├── tests/
│   └── conftest.py
├── .gitignore
├── LICENSE
├── pyproject.toml
├── requirements-dev.txt
├── requirements.txt
└── setup.py
```
### Error Messages

- **`GEMINI_API_KEY not found in environment variables`**: Make sure to set the `GEMINI_API_KEY` environment variable in your `.env` file.
- **`Failed to run Repopack`**: Ensure that Node.js and npm are installed and that Repopack is installed globally.
- **`Failed to configure Gemini client`**: Verify your Gemini API key is correct and that the Generative AI API is enabled in your GCP project.
- **`Failed to generate README`**: There might be an issue with the Gemini model or your codebase content. Try increasing the `MAX_OUTPUT_TOKENS` configuration or simplifying your codebase.
- **`Failed to process directory`**: Ensure the specified directory exists and that you have read access to its contents.
- **`Failed to read file` or `Failed to write file`**: Ensure the specified file paths are correct and that you have read/write permissions.

If you encounter any other errors, please refer to the detailed logs in verbose mode or consult the documentation for more information.

### Troubleshooting

1. **"Command not found" error:**
   - Make sure you've activated the virtual environment
   - Or use the full path to the executable

2. **API Key errors:**
   ```bash
   # Check if .env file exists
   ls -la .env
   
   # Make sure it has the correct content
   cat .env
   # Should show: GEMINI_API_KEY=your_key_here
   ```

3. **Directory permission errors:**
   - Check if you have write permissions in the target directory
   - Try running with `--verbose` flag for more details

4. **Node.js dependency errors:**
   ```bash
   # Reinstall dependencies
   cd /path/to/ReadMe-Generator
   rm -rf node_modules
   pip install -e .
   ```

### Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear and concise messages.
4. Push your branch to your fork.
5. Create a pull request to the main repository.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


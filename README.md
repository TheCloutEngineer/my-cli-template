# Python CLI Template

This is a template design for developing cli apps in
python using the following tools [uv](), [pytest](), and [numpy]().

## How To Get Started

Note: Calculator is added as an example for testing purposes.

```bash
$ uv --version
uv 0.7.7 (Homebrew 2025-05-22)

# Create a packaged application project
$ uv init --package my-uv-tool

# Run the default command
$ cd my-uv-tool
$ uv run my-uv-tool

# ... Write your code (or outsource it to AI) ...
# ... Define the entry points in pyproject.toml ...

# Install the tool
$ uv tool install -e .

# Set up PATH if needed (restart your shell afterward)
$ uv tool update-shell

# Run the command from anywhere
$ my-uv-tool
```

## Testing
To run tests, use the following command:

```bash
uv run pytest --cov --cov-report=html
```


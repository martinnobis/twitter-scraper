# twitter-scraper
A simple twitter scraper

## Development

Create a virtual environment and then install the linters, static code analysers and test tools required for development.

```bash
python3 -m venv env  # Create a virtual environment in env/
env/bin/python -m pip install --upgrade pip  # Update pip to the latest version
env/bin/python -m pip install -r dev_requirements.txt  # Install the development tools
```

### Run linters and static code analysers

```bash
env/bin/python pre_commit.py
```
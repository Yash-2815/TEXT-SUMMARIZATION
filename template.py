import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(filename='script.log', level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'TextSummarizer'

files_list = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in files_list:
    filepath = Path(filepath)
    file_dir = filepath.parent
    file_name = filepath.name

    # Create directory if it doesn't exist
    if file_dir != Path("."):
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir}")

    # Create file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")

from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: [%(message)s]')

project_name = "CNN_Classifier"

list_of_files = [
    ".github/workflows/.git_tmp",
    f'{project_name}/__init__.py',
    f'{project_name}/modules/__init__.py',
    f'{project_name}/utils/__init__.py',
    f'{project_name}/config/__init__.py',
    f'{project_name}/utils/configuration.py',
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/entity/__init__.py',
    f'{project_name}/constants/__init__.py',
    "config/config.yml",
    "dvc.yml",
    "params.yml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file_path in list_of_files:
    filepath = Path(file_path)
    filedir, filename = filepath.parent, filepath.name

    if filedir:
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the file: {filename}')

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
            logging.info(f'Creating empty file: {filepath}')

    else:
        logging.info(f'File: {filename} is already exists')

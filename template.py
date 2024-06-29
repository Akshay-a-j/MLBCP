import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "BreastCancerPred"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"stc/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constatnts/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"

]


for file_path in list_of_files:
    file_path = Path(file_path)
    dirname, filename = os.path.split(file_path)

    if dirname !="":
        os.makedirs(dirname, exist_ok = True)
        logging.info(f"created {dirname} directory")

    if  (not(os.path.exists(file_path)) or (os.path.getsize(file_path))):
        with open(file_path, "w") as file:
            pass
            logging.info(f"file {file_path} is created")

    else:
        logging.info(f"file {file_path} already exists")


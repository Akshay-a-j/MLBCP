from box import ConfigBox
import os
from pathlib import Path
from typing import Any
from ensure import ensure_annotations
import yaml
import logging
from box.exceptions import BoxValueError

@ensure_annotations
def get_size(path: Path) -> str:
    size = round(os.path.getsize(path)/(1024))
    return f"~ {size} KB"

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file {path_to_yaml} is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")

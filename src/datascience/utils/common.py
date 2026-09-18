import os
import yaml
import joblib
from pathlib import Path
from typing import Any
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from src.datascience import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns its content as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the yaml file.

    Raises:
        ValueError: If yaml file is empty.
        e: Any other exception during reading.

    Returns:
        ConfigBox: ConfigBox type object allowing dot-access.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """Creates a list of directories if they don't already exist.

    Args:
        path_to_directories (list): List of paths of directories to create.
        verbose (bool, optional): Whether to log directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data into a JSON file.

    Args:
        path (Path): Path to the json file.
        data (dict): Data to be saved in json file.
    """
    import json

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file content as a ConfigBox.

    Args:
        path (Path): Path to the json file.

    Returns:
        ConfigBox: Key-value data accessed as attributes.
    """
    import json

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves binary data (e.g. trained models or preprocessors) using joblib.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data (e.g. saved models) using joblib.

    Args:
        path (Path): Path to binary file.

    Returns:
        Any: Object stored in the file.
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Calculates file size in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size in KB formatted as string.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
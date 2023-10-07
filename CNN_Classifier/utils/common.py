import json
import base64
from pathlib import Path
from typing import Any

import yaml
import joblib
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from box import ConfigBox

from CNN_Classifier import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns ConfigBox
    Parameters
    ----------
    path_to_yaml
        filepath to the yaml file

    Returns
    -------
    Function return ConfigBox object from box module
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


# @ensure_annotations
# def create_directories(path_to_directories: list, verbose=True) -> None:
#     """
#     Function create directories
#     Parameters
#     ----------
#     path_to_directories
#         list with paths
#     verbose
#         checker for providing logs
#     Returns
#     -------
#     None
#     """
#     for path in path_to_directories:
#         Path(path).mkdir(parents=True, exist_ok=True)
#         if verbose:
#             logger.info(f"created directory at: {path}")

@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Function create directories
    Parameters
    ----------
    path_to_directories
        list with paths
    verbose
        checker for providing logs
    """
    for path in path_to_directories:
        # os.makedirs(path, exist_ok=True)
        Path(path).mkdir(parents=True, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Save dictionary as json file for selected path
    Parameters
    ----------
    path
        path where json should be saved
    data
        dictionary with data which will be store in json file
    Returns
    -------
    None
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f'json file saved at: {path}')


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load json file from selected path
    Parameters
    ----------
    path
        path to json file
    Returns
    -------
    ConfigBox object
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    save data as binary file
    Parameters
    ----------
    data
        Any type of data
    path
        filepath
    Returns
    -------
    None
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Function loads binary file from path
    Parameters
    ----------
    path
        filepath
    Returns
    -------
    Any type of data read from binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Funtion provide the size of the selected file
    Parameters
    ----------
    path
        filepath
    Returns
    -------
    Size of the selected file in KB
    """
    size_in_bytes = path.stat().st_size
    size_in_kb = round(size_in_bytes / 1024)
    return f"~ {size_in_kb} KB"


def decode_image(img_string: str, file_name: str) -> None:
    """
    Function decode image from string and save it in the selected path as image
    Parameters
    ----------
    img_string
        image in base64 format
    file_name
        filepath
    Returns
    -------
    None
    """
    imgdata = base64.b64decode(img_string)
    with open(file_name, 'wb') as f:
        f.write(imgdata)
        f.close()


def encode_image_into_base64(cropped_image_path: str) -> bytes:
    """
    Function convert image into base64 (string) format
    Parameters
    ----------
    cropped_image_path
        path to image

    Returns
    -------
    Image as a string (base64) format
    """
    with open(cropped_image_path, "rb") as f:
        return base64.b64encode(f.read())

"""
Discover methods for drawio_discover

It can not manage more than 40969 levels of folders
"""

import os
from typing import List

from drawio_discover.models.folder import Folder

ALL_LEVELS = 4096


def discover_folders(folder_name: str, level: int = ALL_LEVELS) -> Folder:
    """Discover all packages in a folder

    A package is a folder with an __init__.py file in it.

    :param folder_name: name of the folder to discover
    """
    real_folder_path = os.path.realpath(folder_name)

    is_package = False
    children = []

    for file in os.listdir(folder_name):
        if file == "__init__.py":
            is_package = True
        if level > 0 or level == ALL_LEVELS:
            file_path = os.path.join(real_folder_path, file)
            _scan_sub_folders(file_path, level, children)

    # basename() must be called on the real path to avoid confusion
    # if the folder_name ends_with a "/" that will return ""
    return Folder(
        basename=os.path.basename(real_folder_path),
        real_path=real_folder_path,
        is_package=is_package,
        children=children,
    )


def _scan_sub_folders(file_path: str, level: int, children: List[Folder]):
    """Scan sub folders"""
    if os.path.isdir(file_path):
        folder = discover_folders(file_path, level - 1)
        if folder.basename != "__pycache__":
            children.append(folder)

""" Discover methods for drawio_discover """

import os

from drawio_discover.models.folder import Folder


def discover_folders(folder_name: str):
    """Discover all packages in a folder

    A package is a folder with an __init__.py file in it.
    """
    real_folder_path = os.path.realpath(folder_name)

    is_package = False
    children = []

    for file in os.listdir(folder_name):
        if file == "__init__.py":
            is_package = True
        file_path = os.path.join(real_folder_path, file)
        if os.path.isdir(file_path):
            children.append(discover_folders(file_path))

    return Folder(
        basename=os.path.basename(folder_name),
        real_path=real_folder_path,
        is_package=is_package,
        children=children,
    )

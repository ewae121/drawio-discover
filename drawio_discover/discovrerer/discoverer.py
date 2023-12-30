""" Discover methods for drawio_discover """

import os


def discover_packages(folder_name: str):
    """Discover all packages in a folder

    A package is a folder with an __init__.py file in it.
    """
    package_list = []
    for file, _, files in os.walk(folder_name):
        if "__init__.py" in files:
            package_list.append(file)
    return package_list

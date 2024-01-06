""" Package diagram generation module
"""
from xml.etree.ElementTree import Element
from typing import List

from drawio_discover.models.folder import Folder
from drawio_discover.models.drawio.package import Package
from drawio_discover.diagrams.drawio import (
    init_drawio_file,
)


def generate_package_diagram(folder: Folder) -> Element:
    """Generate the package diagram

    Args:
        folder (Folder): folder to generate the diagram for
        level (int, optional): level of the folder. Defaults to -1.

        -1 means recursive for all levels

    Returns:
        Element: diagram
    """
    elements = generate_package_element(folder)

    file = init_drawio_file(elements)

    return file


def generate_package_element(folder: Folder) -> List[Element]:
    """Generate the package elements for the folder"""
    package = Package(x=40, y=40, parent_cell_id="1", folder=folder)
    return package.get_drawio_package_cells()

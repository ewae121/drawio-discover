""" Drawio file generator module """

from datetime import datetime
from typing import List
import uuid

from xml.etree.ElementTree import Element


def _read_setting_or_default(settings: dict, key: str, default_value: str):
    if key in settings:
        return settings[key]
    return default_value


def init_drawio_file(diagram_elements : List[Element], settings: dict = None) -> Element:
    """Init a drawio file

    Args:
        settings (dict, optional): settings to pass to drawio file. Defaults to None.

    Returns:
        Element: drawio file
    """
    if settings is None:
        settings = {}

    modified_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    diagram_id = str(uuid.uuid4())

    file = Element(
        "mxfile",
        attrib={
            "host": "Electron",
            "modified": modified_date,
            "agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "draw.io/22.1.11 Chrome/114.0.5735.289 Electron/25.9.8 Safari/537.36"
            ),
            "etag": "iZDB-1uGMmguUEppIXjf",
            "version": "22.1.11",
            "type": "device",
        },
    )
    diagram = Element("diagram", attrib={"name": "Page-1", "id": diagram_id})

    mx_graph_model = _init_graph_model(diagram_elements, settings)

    diagram.append(mx_graph_model)
    file.append(diagram)

    return file


def _init_graph_model(diagram_elements : List[Element], settings: dict) -> Element:
    """Init the graph model

    Args:
        settings (dict): contains the settings to pass to the graph model

    Returns:
        Element: graph model
    """
    # pylint: disable=too-many-locals
    dx = _read_setting_or_default(settings, "dx", "1464")
    dy = _read_setting_or_default(settings, "dy", "1027")
    grid = _read_setting_or_default(settings, "grid", "1")
    grid_size = _read_setting_or_default(settings, "gridSize", "10")
    guides = _read_setting_or_default(settings, "guides", "1")
    tooltips = _read_setting_or_default(settings, "tooltips", "1")
    connect = _read_setting_or_default(settings, "connect", "1")
    arrows = _read_setting_or_default(settings, "arrows", "1")
    fold = _read_setting_or_default(settings, "fold", "1")
    page = _read_setting_or_default(settings, "page", "1")
    page_scale = _read_setting_or_default(settings, "pageScale", "1")
    page_width = _read_setting_or_default(settings, "pageWidth", "827")
    page_height = _read_setting_or_default(settings, "pageHeight", "1169")
    background = _read_setting_or_default(settings, "background", "none")
    math = _read_setting_or_default(settings, "math", "0")
    shadow = _read_setting_or_default(settings, "shadow", "0")

    mx_graph_model = Element(
        "mxGraphModel",
        attrib={
            "dx": dx,
            "dy": dy,
            "grid": grid,
            "gridSize": grid_size,
            "guides": guides,
            "tooltips": tooltips,
            "connect": connect,
            "arrows": arrows,
            "fold": fold,
            "page": page,
            "pageScale": page_scale,
            "pageWidth": page_width,
            "pageHeight": page_height,
            "background": background,
            "math": math,
            "shadow": shadow,
        },
    )
    root = Element("root")
    mx_cell = Element("mxCell", attrib={"id": "0"})
    root.append(mx_cell)
    mx_cell1 = Element("mxCell", attrib={"id": "1", "parent": "0"})
    root.append(mx_cell1)
    for element in diagram_elements:
        root.append(element)
    mx_graph_model.append(root)

    return mx_graph_model

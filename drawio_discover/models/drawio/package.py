""" Dataclass for DrawIO packages """

from dataclasses import dataclass
from xml.etree.ElementTree import Element
from uuid import uuid4

from drawio_discover.models.folder import Folder
from drawio_discover.models.drawio.package_properties import (
    DEFAULT_PACKAGE_PROPERTIES as PACKAGE_PROPERTIES,
    TAB_LABEL_X_OFFSET,
    Size,
    EMPTY_PACKAGE_SIZE,
)
from drawio_discover.models.drawio.utils import compute_columns_and_rows_counts


MARGIN_HORIZONTAL = 10
MARGIN_VERTICAL = 10

@dataclass
class Package:
    """Dataclass for Drawio packages"""

    parent_cell_id: str
    x: int
    y: int

    folder: Folder

    def __post_init__(self):
        uuid = self._generate_id()
        self.main_cell_id = f"{uuid}-72"
        self.label_cell_id = f"{uuid}-73"
        self.size = self._compute_size()

    def _generate_id(self) -> str:
        uuid = str(uuid4())
        return uuid.replace("-", "")[16:]

    def get_drawio_package_cells(self):
        """Get the DrawIO cells for the package"""
        tab_properties = PACKAGE_PROPERTIES.tab
        cell_package = Element(
            "mxCell",
            attrib={
                "id": self.main_cell_id,
                "value": "",
                "style": (
                    "shape=folder;fontStyle=1;spacingTop=10;"
                    f"tabWidth={tab_properties.width};tabHeight={tab_properties.height};"
                    "tabPosition=left;"
                    "html=1;rounded=0;shadow=0;comic=0;"
                    "labelBackgroundColor=none;strokeWidth=1;fillColor=none;"
                    "fontFamily=Verdana;fontSize=10;align=center;"
                    "collapsible=1;container=1;"
                ),
                "parent": self.parent_cell_id,
                "vertex": "1",
            },
        )
        cell_package_geometry = Element(
            "mxGeometry",
            attrib={
                "x": str(self.x),
                "y": str(self.y),
                "width": str(self.size.width),
                "height": str(self.size.height),
                "as": "geometry",
            },
        )
        cell_package_geometry_minified = Element(
            "mxRectangle",
            attrib={
                "x": str(self.x),
                "y": str(self.y),
                "width": str(self.size.width),
                "height": str(PACKAGE_PROPERTIES.height_minified),
                "as": "alternateBounds",
            },
        )
        cell_package_geometry.append(cell_package_geometry_minified)
        cell_package.append(cell_package_geometry)

        cell_package_label = Element(
            "mxCell",
            attrib={
                "id": self.label_cell_id,
                "value": self.folder.basename,
                "style": (
                    "text;html=1;align=center;verticalAlign=top;"
                    f"spacingTop=-4;fontSize={PACKAGE_PROPERTIES.label.font_size};"
                    "fontFamily=Verdana",
                ),
                "parent": self.parent_cell_id,
                "vertex": "1",
            },
        )
        cell_package_label_geometry = Element(
            "mxGeometry",
            attrib={
                "x": str(self.x + TAB_LABEL_X_OFFSET),
                "y": str(self.y),
                "width": str(PACKAGE_PROPERTIES.label.width),
                "height": str(PACKAGE_PROPERTIES.label.height),
                "as": "geometry",
            },
        )
        cell_package_label.append(cell_package_label_geometry)

        return cell_package, cell_package_label

    def _compute_size(self) -> Size:
        if not self.folder.children:
            return EMPTY_PACKAGE_SIZE
        columns_count, rows_count = compute_columns_and_rows_counts(self.folder.children)
        width = columns_count * EMPTY_PACKAGE_SIZE.width + columns_count * MARGIN_HORIZONTAL + 2 * MARGIN_HORIZONTAL
        height = rows_count * EMPTY_PACKAGE_SIZE.height + rows_count * MARGIN_VERTICAL + 2 * MARGIN_VERTICAL
        return Size(width=width, height=height)

""" Dataclass for DrawIO packages """

from typing import List
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
from drawio_discover.models.drawio.utils import compute_number_of_columns


MARGIN_HORIZONTAL = 10
MARGIN_VERTICAL = 10

@dataclass
class Package:
    """Dataclass for Drawio packages"""

    parent_cell_id: str

    folder: Folder

    def __post_init__(self):
        uuid = self._generate_id()
        self.main_cell_id = f"{uuid}-72"
        self.label_cell_id = f"{uuid}-73"

        self.children_rows = []
        self._organize_children()

        self.size = self._compute_size()

    def _generate_id(self) -> str:
        uuid = str(uuid4())
        return uuid.replace("-", "")[16:]

    def get_drawio_package_cells(self, x, y):
        """Get the DrawIO cells for the package"""
        cells = []

        tab_properties = PACKAGE_PROPERTIES.tab
        cell_package = Element(
            "mxCell",
            attrib={
                "id": self.main_cell_id,
                "value": self.folder.basename,
                "style": (
                    "shape=folder;fontStyle=1;spacingTop=10;"
                    f"tabWidth={tab_properties.width};tabHeight={tab_properties.height};"
                    "tabPosition=left;"
                    "html=1;rounded=0;shadow=0;comic=0;"
                    "labelBackgroundColor=none;strokeWidth=1;fillColor=none;"
                    "fontFamily=Verdana;fontSize=14;align=center;"
                    "collapsible=1;container=1;movableLabel=1"
                ),
                "parent": self.parent_cell_id,
                "vertex": "1",
            },
        )
        cell_package_geometry = Element(
            "mxGeometry",
            attrib={
                "x": str(x),
                "y": str(y),
                "width": str(self.size.width),
                "height": str(self.size.height),
                "as": "geometry",
            },
        )
        cell_package_geometry_minified = Element(
            "mxRectangle",
            attrib={
                "x": str(x),
                "y": str(y),
                "width": str(self.size.width),
                "height": str(PACKAGE_PROPERTIES.height_minified),
                "as": "alternateBounds",
            },
        )
        cell_package_label_offset = Element(
            "mxPoint",
            attrib={
                "x": str(-24),
                "y": str(-23),
                "as": "offset",
            },
        )

        cell_package_geometry.append(cell_package_geometry_minified)
        cell_package_geometry.append(cell_package_label_offset)
        cell_package.append(cell_package_geometry)

#        cell_package_label = Element(
#            "mxCell",
#            attrib={
#                "id": self.label_cell_id,
#                "value": self.folder.basename,
#                "style": (
#                    "text;html=1;align=center;verticalAlign=top;"
#                    f"spacingTop=-4;fontSize={PACKAGE_PROPERTIES.label.font_size};"
#                    "fontFamily=Verdana",
#                ),
#                "parent": self.parent_cell_id,
#                "vertex": "1",
#            },
#        )
#        cell_package_label_geometry = Element(
#            "mxGeometry",
#            attrib={
#                "x": str(x + TAB_LABEL_X_OFFSET),
#                "y": str(y),
#                "width": str(PACKAGE_PROPERTIES.label.width),
#                "height": str(PACKAGE_PROPERTIES.label.height),
#                "as": "geometry",
#            },
#        )
#        cell_package_label.append(cell_package_label_geometry)

        cells.append(cell_package)
#        cells.append(cell_package_label)

        x = MARGIN_HORIZONTAL
        y = PACKAGE_PROPERTIES.tab.height + MARGIN_VERTICAL

        for row in self.children_rows:
            for child in row:
                cells.extend(child.get_drawio_package_cells(x=x, y=y))
                x += child.size.width + MARGIN_HORIZONTAL
            x = MARGIN_HORIZONTAL
            y += child.size.height + MARGIN_VERTICAL
#        x_index  = 0
#        y_index = 0
#        columns_count, _ = compute_columns_and_rows_counts(self.folder.children)
#        for child in self.folder.children:
#            child_x = MARGIN_HORIZONTAL + x_index * EMPTY_PACKAGE_SIZE.width
#            child_y = PACKAGE_PROPERTIES.tab.height + MARGIN_VERTICAL + y_index * EMPTY_PACKAGE_SIZE.height
#
#            child_package = Package(
#                parent_cell_id=self.main_cell_id,
#                x=child_x,
#                y=child_y,
#                folder=child,
#            )
#            cells.extend(child_package.get_drawio_package_cells())
#
#            if x_index < columns_count:
#                x_index += 1
#            else:
#                x_index = 0
#                y_index += 1
#
        return cells

    def _organize_children(self):
        if not self.folder.children:
            return
        columns_count = compute_number_of_columns(self.folder.children)

        x_index = 0
        row = []
        for child in self.folder.children:
            if x_index >= columns_count:
                x_index = 0
                self.children_rows.append(row)
                row = []

            child_package = Package(
                parent_cell_id=self.main_cell_id,
                folder=child,
            )
            row.append(child_package)
            x_index += 1
        self.children_rows.append(row)

    def _compute_size(self) -> Size:
        if not self.folder.children:
            return EMPTY_PACKAGE_SIZE

        width = MARGIN_HORIZONTAL
        height = MARGIN_VERTICAL

        columns_count = compute_number_of_columns(self.folder.children)

        row_widths = []
        for row in self.children_rows:
            max_child_height = max([child.size.height for child in row]) + len(self.children_rows) * MARGIN_VERTICAL
            row_widths.append(sum([child.size.width for child in row]) + MARGIN_HORIZONTAL)
            for child in row:
                width += child.size.width + MARGIN_HORIZONTAL            
            height += child.size.height + MARGIN_VERTICAL
        max_row_width = max(row_widths) + columns_count * MARGIN_HORIZONTAL
        return Size(width=max_row_width, height=max_child_height)
            

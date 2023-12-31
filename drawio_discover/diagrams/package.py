""" Package diagram generation module
"""
from xml.etree.ElementTree import Element
from typing import List

from drawio_discover.models.folder import Folder
from drawio_discover.diagrams.drawio import (
    init_drawio_file,
)


def generate_package_diagram(folder: Folder, level : int = -1) -> Element:
    """Generate the package diagram

    Args:
        folder (Folder): folder to generate the diagram for
        level (int, optional): level of the folder. Defaults to -1.
        
        -1 means recursive for all levels

    Returns:
        Element: diagram
    """
    elements = generate_package_element(folder, level)
    
    file = init_drawio_file(elements)

    return file

def generate_package_element(folder: Folder, level : int = -1) -> List[Element]:
    """Generate the package diagram for a folder

    Args:
        folder (Folder): folder to generate the diagram for

    Returns:
        Element: diagram
    """

#    mxCell2 = Element("mxCell", attrib={"id":"6e0c8c40b5770093-72", "value":"", "style":"shape=folder;fontStyle=1;spacingTop=10;tabWidth=194;tabHeight=22;tabPosition=left;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeWidth=1;fillColor=none;fontFamily=Verdana;fontSize=10;align=center;", "parent":"1", "vertex":"1"})
#    mxGeometry = Element("mxGeometry", attrib={"x":"39", "y":"40", "width":"761", "height":"1120", "as":"geometry"})
#    mxCell2.append(mxGeometry)
#    
#    mxCell8 = Element("mxCell", attrib={"id":"6e0c8c40b5770093-73", "value":"steve", "style":"text;html=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=10;fontFamily=Verdana", "parent":"1", "vertex":"1"})
#    mxGeometry6 = Element("mxGeometry", attrib={"x":"39", "y":"40", "width":"130", "height":"20", "as":"geometry"})
#    mxCell8.append(mxGeometry6)
#    
#    mxCell9 = Element("mxCell", attrib={"id":"Njk6wq048kB_HqggfJyk-1", "value":"package", "style":"shape=folder;fontStyle=1;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;html=1;whiteSpace=wrap;", "parent":"1", "vertex":"1"})
#    mxGeometry7 = Element("mxGeometry", attrib={"x":"80", "y":"80", "width":"70", "height":"50", "as":"geometry"})
#    mxCell9.append(mxGeometry7)
#    
#    mxCell10 = Element("mxCell", attrib={"id":"JSusr1rjcRLLVGV3j3kc-1", "value":"package", "style":"shape=folder;fontStyle=1;spacingTop=10;tabWidth=40;tabHeight=14;tabPosition=left;html=1;whiteSpace=wrap;", "parent":"1", "vertex":"1"})
#    mxGeometry8 = Element("mxGeometry", attrib={"x":"200", "y":"80", "width":"70", "height":"50", "as":"geometry"})
#    mxCell10.append(mxGeometry8)

    str_x = "39"
    str_y = "40"
    str_width = "761"
    str_height = "1120"
    str_height_minified = "45"
    str_tab_width = "194"
    str_tab_height = "20"

    packageCell = Element("mxCell", attrib={"id":"6e0c8c40b5770093-72", "value":"", "style":f"shape=folder;fontStyle=1;spacingTop=10;tabWidth={str_tab_width};tabHeight={str_tab_height};tabPosition=left;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeWidth=1;fillColor=none;fontFamily=Verdana;fontSize=10;align=center;collapsible=1;container=1;", "parent":"1", "vertex":"1"})
    packageGeometry = Element("mxGeometry", attrib={"x": str_x, "y": str_y, "width": str_width, "height": str_height, "as":"geometry"})
    packageGeometryMinified = Element("mxRectangle", attrib={"x": str_x, "y": str_y, "width":str_width, "height":str_height_minified, "as":"alternateBounds"})
    packageGeometry.append(packageGeometryMinified)
    packageCell.append(packageGeometry)
    
    packageLabelCell = Element("mxCell", attrib={"id":"6e0c8c40b5770093-73", "value":"steve", "style":"text;html=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=14;fontFamily=Verdana", "parent":"1", "vertex":"1"})
    packageLabelCellGeometry = Element("mxGeometry", attrib={"x":str_x, "y":str_y, "width":"191", "height":"22", "as":"geometry"})
    packageLabelCell.append(packageLabelCellGeometry)


#        <mxCell id="6e0c8c40b5770093-72" value="" style="shape=folder;fontStyle=1;spacingTop=10;tabWidth=194;tabHeight=22;tabPosition=left;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeWidth=1;fillColor=none;fontFamily=Verdana;fontSize=10;align=center;collapsible=1;container=1;" parent="1" vertex="1">
#          <mxGeometry x="39" y="10" width="241" height="110" as="geometry">
#            <mxRectangle x="39" y="10" width="241" height="40" as="alternateBounds" />
#          </mxGeometry>
#        </mxCell>
#        <mxCell id="6e0c8c40b5770093-73" value="&lt;b&gt;&lt;font style=&quot;font-size: 14px;&quot;&gt;steve&lt;/font&gt;&lt;/b&gt;" style="text;html=1;align=center;verticalAlign=top;spacingTop=-4;fontSize=10;fontFamily=Verdana" parent="6e0c8c40b5770093-72" vertex="1">
#          <mxGeometry x="9.82" width="180.18" height="1.96" as="geometry" />
#        </mxCell>

    return [packageCell, packageLabelCell]
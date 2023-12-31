"""Utils for the diagrams manipulation
"""

from xml.etree.ElementTree import Element, ElementTree, indent


def generate_file(root_element: Element, file_name: str):
    """Generate the xml file

    The xml file is generated with indentation

    Args:
        root_element (Element): drawio file content(dom)
        file_name (str): file name to generate
    """
    tree = ElementTree(root_element)
    indent(tree)
    tree.write(file_name, encoding="utf-8")


def get_file_content(file_name: str) -> str:
    """Get the content of the file as string"""
    with open(file_name, "r", encoding="utf-8") as myfile:
        data = myfile.read()
        return data

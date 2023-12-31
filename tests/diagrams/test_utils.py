""" This module tests the diagram utils module.
"""

import unittest
import os

from xml.etree.ElementTree import Element
from drawio_discover.diagrams.utils import generate_file, get_file_content


class TestUtils(unittest.TestCase):
    """Tests for the diagram utils module"""

    def test_generate_file(self):
        """Test the generation of the file with indentation"""
        # Create a sample root element
        root_element = Element("root")
        child_element = Element("child")
        root_element.append(child_element)

        # Generate the file
        file_name = "test_file.xml"
        generate_file(root_element, file_name)

        # Read the generated file and check if the content matches
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            self.assertEqual(content, "<root>\n  <child />\n</root>")

    def test_get_file_content(self):
        """Test the get file content function"""
        # Create a sample file
        if os.path.exists("test_file.txt"):
            os.remove("test_file.txt")

        file_name = "test_file.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("This is a test file.")

        # Get the content of the file
        content = get_file_content(file_name)

        # Check if the content matches
        self.assertEqual(content, "This is a test file.")

        # Clean up the test file
        os.remove(file_name)


if __name__ == "__main__":
    unittest.main()

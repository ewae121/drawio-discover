""" Tests for Folder module """

import unittest
from drawio_discover.models.folder import Folder


class TestFolder(unittest.TestCase):
    """Tests for Folder class"""

    def test_folder_creation(self):
        """Test folder creation"""
        folder = Folder("my_folder", "/path/to/folder", True)
        self.assertEqual(folder.basename, "my_folder")
        self.assertEqual(folder.real_path, "/path/to/folder")
        self.assertTrue(folder.is_package)
        self.assertEqual(folder.children, [])

    def test_folder_with_children(self):
        """Test folder with children"""
        child1 = Folder("child1", "/path/to/child1", False)
        child2 = Folder("child2", "/path/to/child2", True)
        folder = Folder("my_folder", "/path/to/folder", True, [child1, child2])
        self.assertEqual(folder.basename, "my_folder")
        self.assertEqual(folder.real_path, "/path/to/folder")
        self.assertTrue(folder.is_package)
        self.assertEqual(len(folder.children), 2)
        self.assertEqual(folder.children[0], child1)
        self.assertEqual(folder.children[1], child2)


if __name__ == "__main__":
    unittest.main()

""" Discoverer tests
"""

import unittest
import os

from drawio_discover.discoverer.discoverer import discover_folders
from drawio_discover.models.folder import Folder


class TestDiscoverer(unittest.TestCase):
    """Test discoverer methods"""

    def test_discover_folders_unexisting(self):
        """Test discoverer with unexisting folder"""
        with self.assertRaises(FileNotFoundError):
            discover_folders("/path/to/empty_folder")

    def _check_folder(self, folder_name, attendee_folder):
        folder = discover_folders(folder_name)

        self.assertEqual(folder.basename, attendee_folder.basename)
        self.assertEqual(folder.real_path, attendee_folder.real_path)
        self.assertEqual(folder.is_package, attendee_folder.is_package)
        self.assertEqual(len(folder.children), len(attendee_folder.children))
        for index, child in enumerate(attendee_folder.children):
            self.assertEqual(folder.children[index], child)

    def test_discover_folders_with_packages(self):
        """Test discoverer with packages

        data folder structure is in tests/data/fake_project
        """
        folder_to_discover = os.path.join(os.getcwd(), "tests/data/fake_project")

        child_not_a_package = Folder(
            basename="not_a_package",
            real_path=os.path.join(folder_to_discover, "not_a_package"),
            is_package=False,
        )
        child_not_a_subpackage = Folder(
            basename="not_a_sub_package",
            real_path=os.path.join(folder_to_discover, "package_a/not_a_sub_package"),
            is_package=False,
        )
        child_sub_package_a = Folder(
            basename="sub_package_a",
            real_path=os.path.join(folder_to_discover, "package_a/sub_package_a"),
            is_package=True,
        )
        child_sub_package_b = Folder(
            basename="sub_package_b",
            real_path=os.path.join(folder_to_discover, "package_a/sub_package_b"),
            is_package=True,
        )
        child_package_a = Folder(
            basename="package_a",
            real_path=os.path.join(folder_to_discover, "package_a"),
            is_package=True,
            children=[child_sub_package_b, child_not_a_subpackage, child_sub_package_a],
        )
        child_package_b = Folder(
            basename="package_b",
            real_path=os.path.join(folder_to_discover, "package_b"),
            is_package=True,
        )

        attendee_folder = Folder(
            basename="fake_project",
            real_path=folder_to_discover,
            is_package=True,
            children=[child_package_a, child_not_a_package, child_package_b],
        )
        self._check_folder(folder_to_discover, attendee_folder)


if __name__ == "__main__":
    unittest.main()

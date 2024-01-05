""" Discoverer tests
"""

import unittest
import os

from drawio_discover.discoverer.discoverer import discover_folders, ALL_LEVELS
from drawio_discover.models.folder import Folder


class TestDiscoverer(unittest.TestCase):
    """Test discoverer methods"""

    def test_discover_folders_unexisting(self):
        """Test discoverer with unexisting folder"""
        with self.assertRaises(FileNotFoundError):
            discover_folders("/path/to/empty_folder")

    def _check_folder(self, folder_name, attendee_folder, level=None):
        if level is None:
            folder = discover_folders(folder_name)
        else:
            folder = discover_folders(folder_name, level)

        self.assertEqual(folder.basename, attendee_folder.basename)
        self.assertEqual(folder.real_path, attendee_folder.real_path)
        self.assertEqual(folder.is_package, attendee_folder.is_package)
        self.assertEqual(len(folder.children), len(attendee_folder.children))
        for index, child in enumerate(attendee_folder.children):
            self.assertEqual(folder.children[index], child)

    def test_discover_folder_empty(self):
        """Test discoverer with empty folder"""
        folder_to_discover = os.path.join(os.getcwd(), "tests/data/empty_folder")
        attendee_folder = Folder(
            basename="empty_folder",
            real_path=folder_to_discover,
            is_package=False,
        )
        self._check_folder(folder_to_discover, attendee_folder)

    def _get_fake_project_structure(self, level=ALL_LEVELS):
        """Get the fake folder structure"""
        folder_to_discover = os.path.join(os.getcwd(), "tests/data/fake_project")
        child_not_a_package = Folder(
            basename="not_a_package",
            real_path=os.path.join(folder_to_discover, "not_a_package"),
            is_package=False,
        )
        if level > 1:
            child_sub_package_a = Folder(
                basename="sub_package_a",
                real_path=os.path.join(folder_to_discover, "package_a/sub_package_a"),
                is_package=True,
            )
            child_not_a_subpackage = Folder(
                basename="not_a_sub_package",
                real_path=os.path.join(
                    folder_to_discover, "package_a/not_a_sub_package"
                ),
                is_package=False,
            )
            child_sub_package_b = Folder(
                basename="sub_package_b",
                real_path=os.path.join(folder_to_discover, "package_a/sub_package_b"),
                is_package=True,
            )
            sub_packages = [
                child_sub_package_b,
                child_sub_package_a,
                child_not_a_subpackage,
            ]
        else:
            sub_packages = []

        child_package_a = Folder(
            basename="package_a",
            real_path=os.path.join(folder_to_discover, "package_a"),
            is_package=True,
            children=sub_packages,
        )
        child_package_b = Folder(
            basename="package_b",
            real_path=os.path.join(folder_to_discover, "package_b"),
            is_package=True,
        )

        if level == 0:
            children = []
        else:
            children = [child_package_a, child_not_a_package, child_package_b]

        attendee_folder = Folder(
            basename="fake_project",
            real_path=folder_to_discover,
            is_package=True,
            children=children,
        )
        return folder_to_discover, attendee_folder

    def _check_fake_folder_with_level(self, level=None):
        if level is None:
            folder_to_discover, attendee_folder = self._get_fake_project_structure()
            self._check_folder(folder_to_discover, attendee_folder)
        else:
            folder_to_discover, attendee_folder = self._get_fake_project_structure(
                level
            )
            self._check_folder(folder_to_discover, attendee_folder, level)

    def test_discover_folders_with_packages(self):
        """Test discoverer with packages and default level

        data folder structure is in tests/data/fake_project
        """
        self._check_fake_folder_with_level()

    def test_discover_folders_with_packages_all_levels(self):
        """Test discoverer with packages with all Levels

        data folder structure is in tests/data/fake_project
        """
        self._check_fake_folder_with_level(ALL_LEVELS)

    def test_discover_folders_with_packages_0_level(self):
        """Test discoverer with packages with 0 Levels -> only root folder

        data folder structure is in tests/data/fake_project
        """
        self._check_fake_folder_with_level(0)

    def test_discover_folders_with_packages_1_level(self):
        """Test discoverer with packages with 1 Levels -> only one level

        data folder structure is in tests/data/fake_project
        """
        self._check_fake_folder_with_level(1)


if __name__ == "__main__":
    unittest.main()

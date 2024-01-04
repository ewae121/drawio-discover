""" Dataclass for folder """

from dataclasses import dataclass, field
from typing import List


@dataclass
class Folder:
    """Dataclass for folder

    - basename: name of the folder
    - real_path: real path of the folder
    - is_package: is the folder a package or not
    """

    basename: str
    real_path: str
    is_package: bool
    children: List["Folder"] = field(default_factory=list)

    def __eq__(self, other):
        if (
            self.basename != other.basename
            or self.real_path != other.real_path
            or self.is_package != other.is_package
        ):
            return False
        if not self.children:
            return self.children == other.children

        if len(self.children) != len(other.children):
            return False

        for idx, child in enumerate(self.children):
            if child != other.children[idx]:
                return False
        return True

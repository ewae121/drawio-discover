""" Dataclasses for DrawIO package properties """

from dataclasses import dataclass

TAB_LABEL_X_OFFSET = 30


@dataclass
class PackageTabProperties:
    """Dataclass for package tab properties"""

    width: int = 194
    height: int = 20


@dataclass
class PackageLabelProperties:
    """
    Dataclass for package label properties
    """

    tab: PackageTabProperties

    font_size: int = 14

    def __post_init__(self):
        self.width = self.tab.width - TAB_LABEL_X_OFFSET
        self.height = self.tab.height


@dataclass
class PackageProperties:
    """Dataclass for package properties"""

    tab: PackageTabProperties = PackageTabProperties()
    label: PackageLabelProperties = PackageLabelProperties(tab)
    height_minified: int = 45


@dataclass
class Size:
    """Dataclass for size"""

    width: int
    height: int

    def __add__(self, other):
        return Size(self.width + other.width, self.height + other.height)


DEFAULT_PACKAGE_PROPERTIES = PackageProperties()

VERTICAL_PAGE_SIZE = Size(width=761, height=1120)
EMPTY_PACKAGE_SIZE = Size(
    width=DEFAULT_PACKAGE_PROPERTIES.tab.width,
    height=DEFAULT_PACKAGE_PROPERTIES.height_minified,
)

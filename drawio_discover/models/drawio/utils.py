""" Utility functions for drawio modules. """

from typing import List
from drawio_discover.models.folder import Folder


def compute_number_of_columns(children: List[Folder]) -> int:
    """
    Compute the number of columns and rows needed to display the given children.
    example 29 will return 7 columns
    """
    count = 1
    while count * count < len(children):
        count += 1
    return count

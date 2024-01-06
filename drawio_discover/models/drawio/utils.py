""" Utility functions for drawio modules. """

from typing import List, Tuple
from drawio_discover.models.folder import Folder

def compute_columns_and_rows_counts(children: List[Folder]) -> Tuple[int, int]:
    """
        Compute the number of columns and rows needed to display the given children.
        example 29 will return 7 columns and 6 rows
    """
    count = 1
    while count * count  <= len(children):
        count += 1
    columns_count = count
    rows_count = count - 1
    return columns_count, rows_count
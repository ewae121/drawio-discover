""" Main module for the application. """

import argparse

from drawio_discover.discoverer.discoverer import discover_folders
from drawio_discover.diagrams.drawio import (
    init_drawio_file,
)
from drawio_discover.diagrams.utils import (
    generate_file,
    get_file_content,
)


def run():
    """Main function for the application."""
    parser = argparse.ArgumentParser(
        prog="drawio-discover",
        description="Help to populate drawio files to make diagrams easily",
        epilog=""" This avoid to scan all folders manually to retrieve code base information. """,
    )
    parser.add_argument("input_folder", help="code base to scan", type=str)
    args = parser.parse_args()

    folder = discover_folders(args.input_folder)
    print(folder)

    file = init_drawio_file()
    generate_file(file, "test.drawio")
    print(get_file_content("test.drawio"))


if __name__ == "__main__":
    run()

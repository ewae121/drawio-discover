""" Main module for the application. """

import argparse

from drawio_discover.discovrerer.discoverer import discover_packages


def run():
    """Main function for the application."""
    parser = argparse.ArgumentParser(
        prog="drawio-discover",
        description="Help to populate drawio files to make diagrams easily",
        epilog=""" This avoid to scan all folders manually to retrieve code base information. """,
    )
    parser.add_argument("input_folder", help="code base to scan", type=str)
    args = parser.parse_args()

    detected_packages = discover_packages(args.input_folder)
    for package in detected_packages:
        print(package)


if __name__ == "__main__":
    run()

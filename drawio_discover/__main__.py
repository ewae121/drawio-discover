""" Main module for the application. """

import argparse


def run():
    """Main function for the application."""
    parser = argparse.ArgumentParser(
        prog="drawio-discover",
        description="Help to populate drawio files to make diagrams easily",
        epilog=""" This avoid to scan all folders manually to retrieve code base information. """,
    )
    parser.add_argument("input_folder", help="code base to scan", type=str)
    args = parser.parse_args()
    print(f"Hello Drawio Discover! scan folder: {args.input_folder}")


if __name__ == "__main__":
    run()

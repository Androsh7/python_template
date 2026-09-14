"""Main entrypoint"""

# Standard libraries
from argparse import ArgumentParser

# Project libraries
from python_template.constants import VERSION


def main():
    parser = ArgumentParser()
    parser.add_argument("--version", action="version", version=f"v{VERSION}")
    args = parser.parse_args()


if __name__ == "__main__":
    main()

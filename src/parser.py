from argparse import ArgumentParser
from typing import Any


def ParseArgs() -> Any:
    argParse: ArgumentParser = ArgumentParser(
        prog="File Organizer",
        description="File Organizer")
    requiredArgs = argParse.add_argument_group("required arguments")
    requiredArgs.add_argument(
        "-d", "--directory",
        type=str,
        required=True,
        help="Directory to organize files in")
    return argParse.parse_args()

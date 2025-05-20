from argparse import ArgumentParser
from datetime import datetime
import os
import sys
from typing import Any
from file_organizer import FileOrganizer
from parser import ParseArgs
import logging

def Main() -> None:
    logger: logging.Logger = logging.getLogger("FileOrganizer")
    if (not os.path.exists("logs")):
        os.mkdir("logs")
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=os.path.join("logs", datetime.strftime(datetime.now(), "%Y-%m-%d.log"))
    )
    
    args = ParseArgs()
    
    if not os.path.exists(args.directory):
        logger.error(f"Incorrect directory at {args.directory}")
        print("This path doesn't exists!")
        sys.exit(0)
    
    file_organizer: FileOrganizer = FileOrganizer(args.directory, logger=logger)    
    file_organizer.organize_files()


if __name__ == "__main__":
    Main()
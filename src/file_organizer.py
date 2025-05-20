import glob
import json
import logging
import os
import shutil
import sys


class FileOrganizer:
    def __init__(self, directory: str, logger: logging.Logger) -> None:
        self.directory: str = directory
        self.logger: logging.Logger = logger
        with open(os.path.join("src", "extensions.json"), "r") as extensions:
            self.extensions: dict[str,str] = json.load(extensions)
        self.logger.info(F"Found {len(self.extensions)} file extensions in extensions.json")

    def organize_files(self) -> None:
        def _ensureFolder(folder_name:str) -> str:
            folder_path: str = os.path.join(self.directory, folder_name)
            if not os.path.exists(folder_path):
                self.logger.info(f"Creating folder {folder_name}")
                os.mkdir(folder_path)
            return folder_path
                
        files: list[str] = self._getFilesInDirectory()
        
        # CONFIRMATION
        confirmation: bool = input(f"Are you sure you want to organize {len(files)} files in directory {self.directory}? [y/N]").lower() == "y"
        self.logger.info(f"Confirmation = {confirmation}")
        if not confirmation:
            print("Exiting")
            sys.exit(1)
        
        for file in files:
            extension: str = os.path.splitext(file)[1][1::]
            folder: str = self.extensions.get(extension, "Misc")
            
            if os.path.isdir(file):
                self.logger.debug(f"{file.lstrip(self.directory)} is a directory")
                folder_path: str = _ensureFolder("Folders")
                shutil.move(file, folder_path)
                
            else:
                self.logger.debug(f"{file.lstrip(self.directory)} is a file of type {self.extensions.get(extension, extension)}")
                folder_path = _ensureFolder(folder)
                shutil.move(file, folder_path)
                

    def _getFilesInDirectory(self) -> list[str]:
        self.logger.info(f"Getting files in directory: {self.directory}")
        files: list[str] = glob.glob(f"{self.directory}/*")
        self.logger.info(f"Found {len(files)} files in directory: {self.directory}")
        sanitized_files: list[str] = []
        for file in files:
            name: str = os.path.basename(file)
            if name in set(list(self.extensions.values()) + ["Folders", "Misc"]):
                print("EXISTING -",name)
                self.logger.info("Found existing organization folder {name}; skipping...")
            else:
                print(name)
                sanitized_files.append(file)
        
        return sanitized_files
        
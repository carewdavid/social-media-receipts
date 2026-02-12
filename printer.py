from typing import BinaryIO, Dict


class Printer:
    """Represent an ESC/POS line printer"""
    config: Dict
    file_handle: BinaryIO
    
    def __init__(self, path: str, config: Dict):
        self.config = config
        #TODO make sure things get cleaned up properly. Possibly by making this class a context manager.
        #In the meantime, we tell ourselves its okay because this file will be open for the lifetime of the program. We can't do anything without it
        self.file_handle = open(path, "wb") 

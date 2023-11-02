from abc import ABC, abstractmethod
from pydantic import BaseModel

class FileDataService(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def get_data(query: BaseModel):
        pass
from managers.data_managers import DataManager
from abc import ABC, abstractmethod
from pydantic import BaseModel

class AbstractLogService(ABC):
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

    @abstractmethod
    def get_data(query: BaseModel):
        pass


class CSVLogService(AbstractLogService): 
    def get_data(self, query: BaseModel):
        return self.data_manager.read_data(query)
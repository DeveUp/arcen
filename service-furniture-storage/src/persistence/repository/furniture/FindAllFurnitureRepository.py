from operator import ge
from src.persistence.repository.IRepository import IRepository

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.database import get_db

class FindAllFurnitureRepository(IRepository):

    def __init__(self):
        self.db = get_db()

    def execute(self, data:dict):
        return None
from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.database import get_db
from src.util.constant import COLUMN_FURNITURE, COLUMN_FURNITURE_ID

class UpdateFurnitureRepository(IRepository):

    def __init__(self):
        self.db = get_db()

    def execute(self, data:dict):
        id = data[COLUMN_FURNITURE_ID]
        furniture = data[COLUMN_FURNITURE]
        return None
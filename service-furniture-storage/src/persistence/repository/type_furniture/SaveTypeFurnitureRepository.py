from src.persistence.repository.IRepository import IRepository
from src.persistence.database.database import get_db
from src.util.constant import COLUMN_TYPE_FURNITURE

class SaveTypeFurnitureRepository(IRepository):

    def __init__(self):
        self.db = get_db()

    def execute(self, data:dict):
        try:
            type_furniture = dict(data[COLUMN_TYPE_FURNITURE])
        except:
            type_furniture= None
        return type_furniture
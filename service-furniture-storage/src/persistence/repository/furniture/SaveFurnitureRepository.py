from src.persistence.repository.IRepository import IRepository
from src.persistence.database.database import get_db
from src.util.constant import COLUMN_FURNITURE, COLUMN_FURNITURE_ID

class SaveFurnitureRepository(IRepository):

    def __init__(self):
        self.db = get_db()

    def execute(self, data:dict):
        try:
            furniture = dict(data[COLUMN_FURNITURE])
        except:
            furniture= None
        return furniture
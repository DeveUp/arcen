from webbrowser import get
from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.database import get_db
from src.util.constant import COLUMN_TYPE_FURNITURE, COLUMN_TYPE_FURNITURE_ID

class UpdateTypeFurnitureRepository(IRepository):

    def __init__(self):
        self.db = get_db()

    def execute(self, data:dict):
        id = data[COLUMN_TYPE_FURNITURE_ID]
        type_furniture = data[COLUMN_TYPE_FURNITURE]
        return None
from xml.dom.minidom import Element
from sqlalchemy.orm import Session

from src.model.entity.Block import Block
from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_BLOCK, COLUMN_BLOCK_ID

class UpdateBlockRepository(IRepository):

    def __init__(self, db:Session):
        self.db = db

    def execute(self, data:dict):
        id = data[COLUMN_BLOCK_ID]
        element = data[COLUMN_BLOCK]
        find_by_id = self.db.query(Block).get(id)
        find_by_id = self.to_exchange(find_by_id, element)
        self.db.commit()
        self.db.refresh(find_by_id)
        return find_by_id
    
    def to_exchange(self, data, element): 
        data.letter = element.letter
        data.flat = element.flat
        return data
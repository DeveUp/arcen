from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.block.FindAllBlockRepository import FindAllBlockRepository
from src.persistence.schema.BlockSchema import BlockSchema

class FindAllBlockService(IService):

    def __init__(self, db:Session):
        self.repository = FindAllBlockRepository(db)
        self.schema = BlockSchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)
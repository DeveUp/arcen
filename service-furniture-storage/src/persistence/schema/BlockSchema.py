from src.model.entity.Block import Block
from src.model.response.BlockResponse import BlockResponse
from src.util.constant import COLUMN_BLOCK_ID, COLUMN_BLOCK_LETTER, COLUMN_BLOCK_FLAT, COLUMN_BLOCK_CREATION_DATE
from src.util.common import get_validate_field

class BlockSchema:

    def __init__(self):
        self.id = COLUMN_BLOCK_ID
        self.letter = COLUMN_BLOCK_LETTER
        self.flat = COLUMN_BLOCK_FLAT
        self.creation_date = COLUMN_BLOCK_CREATION_DATE

    def entity(self, object) -> Block:
        if object == None: 
            return object
        return object
        
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def response(self, object) -> BlockResponse:
        if object == None: 
            return object
        return BlockResponse(
            id = object.id,
            letter= object.letter,
            flat= object.flat,
            date= object.date,
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_BLOCK_ID: object.id,
            COLUMN_BLOCK_LETTER: object.letter, 
            COLUMN_BLOCK_FLAT: object.flat, 
            COLUMN_BLOCK_CREATION_DATE: object.creation_date,
        }
        if create != None:
            data[self.creation_date]= create
        return data
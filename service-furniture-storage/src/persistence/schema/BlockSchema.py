from src.model.entity.Block import Block
from src.model.dto.BlockDto import BlockDto
from src.util.constant import COLUMN_BLOCK_ID, COLUMN_BLOCK_LETTER, COLUMN_BLOCK_FLAT, COLUMN_BLOCK_CREATION_DATE

class BlockSchema:

    def __init__(self):
        self.id = COLUMN_BLOCK_ID
        self.letter = COLUMN_BLOCK_LETTER
        self.flat = COLUMN_BLOCK_FLAT
        self.creation_date = COLUMN_BLOCK_CREATION_DATE

    def block(self, block) -> Block:
        if block == None: 
            return block
        entity = Block(
            COLUMN_BLOCK_ID = str(block[self.id]),
            COLUMN_BLOCK_LETTER = block[self.letter],
            COLUMN_BLOCK_FLAT = block[self.flat],
            COLUMN_BLOCK_CREATION_DATE = block[self.creation_date]
        )
        return entity
    
    def blocks(self, blocks) -> list:
        if blocks == None: 
            return blocks
        return [self.block(block) for block in blocks]
    
    def block_dto(self, block) -> BlockDto:
        if block == None: 
            return block
        return BlockDto(
            COLUMN_BLOCK_LETTER = block[self.letter], 
            COLUMN_BLOCK_FLAT = block[self.flat], 
            COLUMN_BLOCK_CREATION_DATE = block[self.creation_date]
        )

    def block_dict(self, block, create= None) -> dict:
        if block == None: 
            return block
        try:
            id = block[self.id]
        except:
            id = None
        try:
            creation_date = block[self.creation_date]
        except:
            creation_date = None
        data = {
            self.letter: block[self.letter],
            self.flat: block[self.flat]
        }
        if id != None:
            data[self.id]= id
        if creation_date != None:
            data[self.creation_date]= creation_date
        if create != None:
            data[self.creation_date]= create
        return data
from src.model.entity.Block import Block
from src.model.dto.BlockDto import BlockDto
from src.util.constant import COLUMN_BLOCK_ID, COLUMN_BLOCK_LETTER, COLUMN_BLOCK_FLAT, COLUMN_BLOCK_DATE

class BlockSchema:

    def __init__(self):
        self.id = COLUMN_BLOCK_ID
        self.letter = COLUMN_BLOCK_LETTER
        self.flat = COLUMN_BLOCK_FLAT
        self.date = COLUMN_BLOCK_DATE

    def block(self, block) -> Block:
        if block == None: 
            return block
        entity = Block()
        entity.set_id(str(block[self.id]))
        entity.set_letter(block[self.letter])
        entity.set_flat(block[self.flat])
        entity.set_date(block[self.date])
        return entity
    
    def blocks(self, blocks) -> list:
        if blocks == None: 
            return blocks
        return [self.block(block) for block in blocks]
    
    def block_dto(self, block) -> BlockDto:
        if block == None: 
            return block
        return BlockDto(
            letter = block[self.letter], 
            flat = block[self.flat], 
            date = block[self.date]
        )

    def block_dict(self, block, create= None) -> dict:
        if block == None: 
            return block
        try:
            id = block[self.id]
        except:
            id = None
        try:
            date = block[self.date]
        except:
            date = None
        data = {
            self.letter: block[self.letter],
            self.flat: block[self.flat]
        }
        if id != None:
            data[self.id]= id
        if date != None:
            data[self.date]= date
        if create != None:
            data[self.date]= create
        return data
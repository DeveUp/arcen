from src.model.entity.Dependence import Dependence
from src.model.dto.DependenceDto import DependenceDto
from src.util.constant import COLUMN_DEPENDENCE_ID, COLUMN_DEPENDENCE_NAME, COLUMN_DEPENDENCE_CODE

class DependenceSchema:

    def __init__(self):
        self.id = COLUMN_DEPENDENCE_ID
        self.name = COLUMN_DEPENDENCE_NAME
        self.code = COLUMN_DEPENDENCE_CODE

    def dependence(self, dependence) -> Dependence:
        if dependence == None: 
            return dependence
        return dependence
        
    def dependence_other(self, dependence) -> Dependence:
        if dependence == None: 
            return dependence
        entity = Dependence(
            COLUMN_DEPENDENCE_ID = dependence[self.id],
            COLUMN_DEPENDENCE_NAME = dependence[self.name],
            COLUMN_DEPENDENCE_CODE = dependence[self.code]
        )
        return entity

    def dependences(self, dependences) -> list:
        if dependences == None: 
            return dependences
        return [self.dependence(dependence) for dependence in dependences]
    
    def dependence_dto(self, dependence) -> DependenceDto:
        if dependence == None: 
            return dependence
        return DependenceDto(
            COLUMN_DEPENDENCE_NAME = dependence[self.name],
            COLUMN_DEPENDENCE_CODE = dependence[self.code]
        )

    def dependence_dict(self, dependence, create= None) -> dict:
        if dependence == None: 
            return dependence
        try:
            id = dependence[self.id]
        except:
            id = None
        data = {
            self.name: dependence[self.name],
            self.code: dependence[self.code]
        }
        if id != None:
            data[self.id]= id
        return data
import os
import httpx
from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.Shelf.SaveShelfRepository import SaveShelfRepository
from src.service.type_shelf.FindByIdTypeShelfService import FindByIdTypeShelfService
from src.service.dependence.FindByIdDependenceService import FindByIdDependenceService
from src.persistence.schema.ShelfSchema import ShelfSchema
#from src.util.constant import get_TypeShelfId
from src.util.constant import COLUMN_TYPE_SHELF_ID,COLUMN_DEPENDENCE_ID, RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TYPE_SHELF_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT

class SaveShelfService(IService):

    def __init__(self, db: Session):
        self.repository = SaveShelfRepository(db)
        self.repositoryTypeShelf = FindByIdTypeShelfService(db);
        self.repositoryDependence = FindByIdDependenceService(db);
        self.schema = ShelfSchema()

    def execute(self, data:dict):
        shelf = data.get("shelf")
        typeShelfId = shelf.id_type_shelf
        dataType = dict({COLUMN_TYPE_SHELF_ID:typeShelfId})
        dependenceId = shelf.id_dependence
        dataDependence = dict({COLUMN_DEPENDENCE_ID:dependenceId})
        CAST_SERVICE_HOST_URL = 'http://localhost:8002/api/furniture/'
        url = os.environ.get('CAST_SERVICE_HOST_URL') or CAST_SERVICE_HOST_URL
        r = httpx.get(f'{url}{shelf.id_furniture}')
        c = True if r.status_code == 200 else False
        print(r)
        if self.repositoryTypeShelf.execute(dataType) == None:
            raise HTTPException(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TYPE_SHELF_FIND_BY_ID_NOT_CONTENT)
        if self.repositoryDependence.execute(dataDependence) == None:
            raise HTTPException(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT)
        if c == False:
            raise HTTPException(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,"No se encontro el mueble")
        try:
            #print(data)
            
            element = self.repository.execute(data)
            element = self.schema.shelf(element)
        except:
            element= None
        return element

from src.util.constant import COLUMN_TYPE_SHELF_ID
from sqlalchemy.orm import Session
from src.service.type_shelf.FindByIdTypeShelfService import FindByIdTypeShelfService



def get_TypeShelfId (shelf, db: Session):
    print("GetGregorio")
    repositoryTypeShelf = FindByIdTypeShelfService(db);
    typeShelfId = shelf.id_type_shelf
    dataType = dict({COLUMN_TYPE_SHELF_ID:typeShelfId})
    return repositoryTypeShelf.execute(dataType)

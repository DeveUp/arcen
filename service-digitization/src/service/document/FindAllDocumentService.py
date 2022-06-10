from src.service.IService import IService
from src.persistence.repository.document.FindAllDocumentRepository import FindAllDocumentRepository
from src.persistence.schema.DocumentSchema import DocumentSchema

class FindAllDocumentService(IService):

    def __init__(self):
        self.repository = FindAllDocumentRepository()
        self.schema = DocumentSchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)
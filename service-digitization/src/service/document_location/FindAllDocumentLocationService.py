from src.service.IService import IService
from src.persistence.repository.document_location.FindAllDocumentLocationRepository import FindAllDocumentLocationRepository
from src.persistence.schema.DocumentLocationSchema import DocumentLocationSchema

class FindAllDocumentLocationService(IService):

    def __init__(self):
        self.repository = FindAllDocumentLocationRepository()
        self.schema = DocumentLocationSchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)
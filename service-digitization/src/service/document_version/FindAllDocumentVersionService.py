from src.service.IService import IService

from src.persistence.repository.document_version.FindAllDocumentVersionRepository import FindAllDocumentVersionRepository
from src.persistence.schema.DocumentVersionSchema import DocumentVersionSchema

class FindAllDocumentVersionService(IService):

    def __init__(self):
        self.repository = FindAllDocumentVersionRepository()
        self.schema = DocumentVersionSchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)
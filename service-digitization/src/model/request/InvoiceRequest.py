"""
    @description - Peticion folio
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

class InvoiceRequest(BaseModel):
    name: str
    index_number: int
    id_invoice_statu: str
    security_level: int
    date:str
"""
    @name - SaveFurnitureService
    @description - Servicio para registrar un mueble
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.model.entity.Furniture import Furniture

from src.feign.AuditFeign import AuditFeign

from src.service.IService import IService
from src.service.block.FindByIdBlockService import FindByIdBlockService
from src.service.type_furniture.FindByIdTypeFurnitureService import FindByIdTypeFurnitureService

from src.persistence.repository.furniture.SaveFurnitureRepository import SaveFurnitureRepository
from src.persistence.schema.FurnitureSchema import FurnitureSchema

from src.util.constant import RESPONSE
from src.util.constant import DATABASE
from src.util.constant import FEIGN
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error

class SaveFurnitureService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = SaveFurnitureRepository(db)
        self.find_by_id_block = FindByIdBlockService(db)
        self.find_by_id_type_furniture = FindByIdTypeFurnitureService(db)
        self.schema = FurnitureSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['furniture']
        self.current_operation = FEIGN['type']['generic']['post']['save']

    # @override
    # @method - Registra un mueble
    # @parameter - data - Json con el mueble a registrar
    # @return - Furniture
    def execute(self, data:dict):
        try:
            self.dependence(data)
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except HTTPException as error_http:
            feign_audit_save_error(
                self.feign_audit,
                self.current_service,
                self.current_operation,
                feign_audit_build_error(error_http.status_code, error_http.detail)
            )
        except:
            feign_audit_save_error(
                self.feign_audit,
                self.current_service,
                self.current_operation,
                RESPONSE['furniture']['post']['save']['error']['default']
            )
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            element
        )
        return element

    # @method - Verifica la depedencia del objecto
    # @parameter - data - Json con el mueble a validar
    # @return - list
    def dependence(self, data):
        furniture:Furniture = Furniture(**dict(data[DATABASE['table']['furniture']['name']]))
        # Consulta que exista un bloque con ese pk
        block = self.find_by_id_block.execute(dict({
            DATABASE['table']['block']['pk']: str(furniture.id_block)
        }))
        # Consulta que exista un tipo de mueble con ese pk
        type_furniture = self.find_by_id_type_furniture.execute(dict({
            DATABASE['table']['type_furniture']['pk']: str(furniture.id_type_furniture)
        }))
        return [block, type_furniture]
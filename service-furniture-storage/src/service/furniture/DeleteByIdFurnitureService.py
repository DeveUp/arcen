"""
    @name - DeleteByIdFurnitureService
    @description - Servicio para eliminar un mueble
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign

from src.service.IService import IService

from src.persistence.schema.FurnitureSchema import FurnitureSchema
from src.persistence.repository.furniture.FindByIdFurnitureRepository import FindByIdFurnitureRepository
from src.persistence.repository.furniture.DeleteByIdFurnitureRepository import DeleteByIdFurnitureRepository

from src.util.constant import DATABASE
from src.util.constant import FEIGN 
from src.util.constant import RESPONSE
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error

class DeleteByIdFurnitureService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.find_by_id = FindByIdFurnitureRepository(db)
        self.repository = DeleteByIdFurnitureRepository(db)
        self.schema = FurnitureSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['furniture']
        self.current_operation = FEIGN['type']['generic']['delete']['delete_by_id']

    # @override
    # @method - Elimina un mueble por su pk
    # @parameter - data - Json con el pk del mueble a eliminar
    # @return - Void
    def execute(self, data:dict): 
        furniture = self.find_by_id_furniture(data)
        data = dict({
            DATABASE['table']['furniture']['name']: furniture
        })
        try:
            element = self.repository.execute(data)
        except HTTPException as error_http:
            feign_audit_save_error(
                self.feign_audit,
                self.current_service,
                self.current_operation,
                feign_audit_build_error(error_http.status_code, error_http.detail)
            )
        except:
            element = False
        finally:
            if element == False:
                feign_audit_save_error(
                    self.feign_audit,
                    self.current_service,
                    self.current_operation,
                    RESPONSE['furniture']['delete']['delete_by_id']['error']['default']
                )
            else:
                furniture = self.schema.response(furniture)   
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            furniture
        )
        return element
    
    # @method - Consulta un mueble por su pk
    # @parameter - data - Json con el pk del mueble
    # @return - Furniture
    def find_by_id_furniture(self, data): 
        try:
            element = self.find_by_id.execute(data)
        except HTTPException as error_http:
            feign_audit_save_error(
                self.feign_audit,
                self.current_service,
                self.current_operation,
                feign_audit_build_error(error_http.status_code, error_http.detail)
            )
        except:
            element = None
        finally:
            if element == None:
                feign_audit_save_error(
                    self.feign_audit,
                    self.current_service,
                    self.current_operation,
                    RESPONSE['furniture']['get']['find_by_id']['error']['default']
                )
        return element
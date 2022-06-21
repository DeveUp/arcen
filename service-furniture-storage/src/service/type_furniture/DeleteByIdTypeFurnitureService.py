"""
    @name - DeleteByIdTypeFurnitureService
    @description - Servicio para eliminar un tipo de mueble
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

from src.persistence.repository.type_furniture.FindByIdTypeFurnitureRepository import FindByIdTypeFurnitureRepository
from src.persistence.repository.type_furniture.DeleteByIdTypeFurnitureRepository import DeleteByIdTypeFurnitureRepository
from src.persistence.schema.TypeFurnitureSchema import TypeFurnitureSchema

from src.util.constant import DATABASE
from src.util.constant import FEIGN 
from src.util.constant import RESPONSE
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error

class DeleteByIdTypeFurnitureService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.find_by_id = FindByIdTypeFurnitureRepository(db)
        self.repository = DeleteByIdTypeFurnitureRepository(db)
        self.schema = TypeFurnitureSchema()
         # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['type_furniture']
        self.current_operation = FEIGN['type']['generic']['delete']['delete_by_id']

    # @override
    # @method - Elimina un tipo de mueble por su pk
    # @parameter - data - Json con el pk del tipo de mueble a eliminar
    # @return - Void
    def execute(self, data:dict): 
        type_furniture = self.find_by_id_type_furniture(data)
        data = dict({
            DATABASE['table']['type_furniture']['name']: type_furniture
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
                    RESPONSE['type_furniture']['delete']['delete_by_id']['error']['default']
                )
            else:
                type_furniture = self.schema.response(type_furniture)   
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            type_furniture
        )
        return element
    
    # @method - Consulta un tipo de mueble por su pk
    # @parameter - data - Json con el pk del tipo de mueble
    # @return - TypeFurniture
    def find_by_id_type_furniture(self, data): 
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
                    RESPONSE['type_furniture']['get']['find_by_id']['error']['default']
                )
        return element
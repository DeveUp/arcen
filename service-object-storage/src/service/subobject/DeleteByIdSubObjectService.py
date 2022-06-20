"""
    @name - DeleteByIdSubObjectService
    @description - Servicio para eliminar un subobjeto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.service.IService import IService

from src.feign.AuditFeign import AuditFeign 

from src.persistence.repository.subobject.FindByIdSubObjectRepository import FindByIdSubObjectRepository
from src.persistence.repository.subobject.DeleteByIdSubObjectRepository import DeleteByIdSubObjectRepository
from src.persistence.schema.SubObjectSchema import SubObjectSchema

from src.util.constant import DATABASE
from src.util.constant import FEIGN 
from src.util.constant import RESPONSE
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error

class DeleteByIdSubObjectService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.find_by_id = FindByIdSubObjectRepository(db)
        self.repository = DeleteByIdSubObjectRepository(db)
        self.schema:SubObjectSchema = SubObjectSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['subobject']
        self.current_operation = FEIGN['type']['generic']['delete']['delete_by_id']

    # @override
    # @method - Elimina un subobjeto por su pk
    # @parameter - data - Json con el pk del subobjeto a eliminar
    # @return - SubObject
    def execute(self, data:dict): 
        object = self.find_by_id_subobject(data)
        data = dict({
            DATABASE['table']['subobject']['name']: object
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
                    RESPONSE['subobject']['delete']['delete_by_id']['error']['default']
                )
            else:
                object = self.schema.response(object)   
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            object
        )
        return element
    
    # @method - Consulta un subobjeto por su pk
    # @parameter - data - Json con el pk del subobjeto
    # @return - SubObject
    def find_by_id_subobject(self, data): 
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
                    RESPONSE['subobject']['get']['find_by_id']['error']['default']
                )
        return element
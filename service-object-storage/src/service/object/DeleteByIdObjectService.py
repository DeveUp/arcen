"""
    @name - DeleteByIdObjectService
    @description - Servicio para eliminar un objecto
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

from src.persistence.repository.object.FindByIdObjectRepository import FindByIdObjectRepository
from src.persistence.repository.object.DeleteByIdObjectRepository import DeleteByIdObjectRepository
from src.persistence.schema.ObjectSchema import ObjectSchema

from src.util.constant import DATABASE
from src.util.constant import FEIGN 
from src.util.constant import RESPONSE
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error


class DeleteByIdObjectService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.find_by_id = FindByIdObjectRepository(db)
        self.repository = DeleteByIdObjectRepository(db)
        self.schema:ObjectSchema = ObjectSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['object']
        self.current_operation = FEIGN['type']['generic']['delete']['delete_by_id']

    # @override
    # @method - Elimina un objecto por su pk
    # @parameter - data - Json con el pk del objecto a eliminar
    # @return - Void
    def execute(self, data:dict): 
        object = self.find_by_id_object(data)
        data = dict({
            DATABASE['table']['object']['name']: object
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
                    RESPONSE['object']['delete']['delete_by_id']['error']['default']
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
    
    # @method - Consulta un objecto por su pk
    # @parameter - data - Json con el pk del objecto
    # @return - Object
    def find_by_id_object(self, data): 
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
                    RESPONSE['object']['get']['find_by_id']['error']['default']
                )
        return element
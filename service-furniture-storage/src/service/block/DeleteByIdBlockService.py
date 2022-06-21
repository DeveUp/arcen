"""
    @name - DeleteByIdBlockService
    @description - Servicio para eliminar un bloque
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

from src.persistence.schema.BlockSchema import BlockSchema
from src.persistence.repository.block.FindByIdBlockRepository import FindByIdBlockRepository
from src.persistence.repository.block.DeleteByIdBlockRepository import DeleteByIdBlockRepository
from src.persistence.schema.BlockSchema import BlockSchema

from src.util.constant import DATABASE
from src.util.constant import FEIGN 
from src.util.constant import RESPONSE
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error

class DeleteByIdBlockService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.find_by_id = FindByIdBlockRepository(db) 
        self.repository = DeleteByIdBlockRepository(db)
        self.schema = BlockSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['block']
        self.current_operation = FEIGN['type']['generic']['delete']['delete_by_id']

    # @override
    # @method - Elimina un bloque por su pk
    # @parameter - data - Json con el pk del bloque a eliminar
    # @return - Void
    def execute(self, data:dict): 
        block = self.find_by_id_block(data)
        data = dict({
            DATABASE['table']['block']['name']: block
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
                    RESPONSE['block']['delete']['delete_by_id']['error']['default']
                )
            else:
                block = self.schema.response(block)   
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            block
        )
        return element
    
    # @method - Consulta un bloque por su pk
    # @parameter - data - Json con el pk del bloque
    # @return - Block
    def find_by_id_block(self, data): 
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
                    RESPONSE['block']['get']['find_by_id']['error']['default']
                )
        return element
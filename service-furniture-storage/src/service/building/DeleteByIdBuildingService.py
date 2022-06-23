"""
    @name - DeleteByIdBuildingService
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

from src.persistence.schema.BuildingSchema import BuildingSchema
from src.persistence.repository.building.FindByIdBuildingRepository import FindByIdBuildingRepository
from src.persistence.repository.building.DeleteByIdBuildingRepository import DeleteByIdBuildingRepository
from src.persistence.schema.BlockSchema import BlockSchema

from src.util.constant import DATABASE
from src.util.constant import FEIGN 
from src.util.constant import RESPONSE
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error

class DeleteByIdBuildingService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.find_by_id = FindByIdBuildingRepository(db) 
        self.repository = DeleteByIdBuildingRepository(db)
        self.schema = BuildingSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['building']
        self.current_operation = FEIGN['type']['generic']['delete']['delete_by_id']

    # @override
    # @method - Elimina un edificio por su pk
    # @parameter - data - Json con el pk del edificio a eliminar
    # @return - Void
    def execute(self, data:dict): 
        block = self.find_by_id_building(data)
        data = dict({
            DATABASE['table']['building']['name']: block
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
                    RESPONSE['building']['delete']['delete_by_id']['error']['default']
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
    
    # @method - Consulta un edificio por su pk
    # @parameter - data - Json con el pk del edificio
    # @return - Building
    def find_by_id_building(self, data): 
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
                    RESPONSE['building']['get']['find_by_id']['error']['default']
                )
        return element
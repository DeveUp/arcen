"""
    @name - SaveBuildingService
    @description - Servicio para registrar un edificio
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-27
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign

from src.model.entity.Building import Building

from src.service.IService import IService
from src.service.building.FindByNameAndFlatBuildingService import FindByNameAndFlatBuildingService

from src.persistence.repository.building.SaveBuildingRepository import SaveBuildingRepository
from src.persistence.schema.BuildingSchema import BuildingSchema

from src.util.constant import RESPONSE
from src.util.constant import FEIGN
from src.util.constant import DATABASE
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error
from src.util.common import get_exception_http

class SaveBlockService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = SaveBuildingRepository(db)
        self.find_by_name_and_flat_building = FindByNameAndFlatBuildingService(db)
        self.schema = BuildingSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['building']
        self.current_operation = FEIGN['type']['generic']['post']['save']

    # @override
    # @method - Registra un edificio
    # @parameter - data - Json con el edificio a registrar
    # @return - Building
    def execute(self, data:dict):
        try:
            self.depedencies(data)
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
                RESPONSE['building']['post']['save']['error']['default']
            )
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            element
        )
        return element

    # @method - Verifica la depedencia del edificio
    # @parameter - data - Json con el edificio a validar
    # @return - Void
    def depedencies(self, data):
        building = Building(**dict(data[DATABASE['table']['building']['name']]))
        self.building_by_name_and_flat(building)

    # @method - Verifica si existe un edificio con un nombre en un piso
    # @parameter - building - Informacion del edificio
    # @return - Void
    def building_by_name_and_flat(self, building:Building):
        try:
            building_name_and_flat = self.find_by_name_and_flat_building .execute(dict({
                DATABASE['table']['building']['column'][1]: str(building.name),
                DATABASE['table']['building']['column'][4]: str(building.flat)
            }))
        except HTTPException:
            building_name_and_flat = None
        except:
            building_name_and_flat = None
        finally:
            if building_name_and_flat != None:
                raise get_exception_http(RESPONSE['building']['post']['save']['error']['name_and_flat'])
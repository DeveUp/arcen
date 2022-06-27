"""
    @name - SaveBlockService
    @description - Servicio para registrar un bloque
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign

from src.model.entity.Block import Block

from src.service.IService import IService
from src.service.building.FindByIdBuildingService import FindByIdBuildingService
from src.service.block.FindByLetterAndFlatBlockService import FindByLetterAndFlatBlockService

from src.persistence.repository.block.SaveBlockRepository import SaveBlockRepository
from src.persistence.schema.BlockSchema import BlockSchema

from src.util.constant import RESPONSE
from src.util.constant import FEIGN
from src.util.constant import DATABASE
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error
from src.util.common import get_exception_http

class SaveBlockService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = SaveBlockRepository(db)
        self.find_by_id_building = FindByIdBuildingService(db)
        self.find_by_letter_and_flat_block = FindByLetterAndFlatBlockService(db)
        self.schema = BlockSchema()
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['block']
        self.current_operation = FEIGN['type']['generic']['post']['save']

    # @override
    # @method - Registra un bloque
    # @parameter - data - Json con el bloque a registrar
    # @return - Block
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
                RESPONSE['block']['post']['save']['error']['default']
            )
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            element
        )
        return element

    # @method - Verifica la depedencia del bloque
    # @parameter - data - Json con el bloque a validar
    # @return - list
    def depedencies(self, data):
        block = Block(**dict(data[DATABASE['table']['block']['name']]))
        # Se verifica si ya existe un piso con esa letra
        self.block_by_letter_and_flat(block)
        # Se consulta si existe un edificio con ese pk
        building  = self.find_by_id_building.execute(dict({
            DATABASE['table']['building']['pk']: str(block.id_building)
        }))
        return [building]
    
    # @method - Verifica si existe un bloque con una letra en un piso
    # @parameter - block - Informacion del bloque
    # @return - Void
    def block_by_letter_and_flat(self, block:Block):
        try:
            block_letter_and_flat = self.find_by_letter_and_flat_block.execute(dict({
                DATABASE['table']['block']['column'][1]: str(block.letter),
                DATABASE['table']['block']['column'][2]: str(block.flat)
            }))
        except HTTPException:
            block_letter_and_flat = None
        except:
            block_letter_and_flat = None
        finally:
            if block_letter_and_flat != None:
                raise get_exception_http(RESPONSE['block']['post']['save']['error']['letter_and_flat'])

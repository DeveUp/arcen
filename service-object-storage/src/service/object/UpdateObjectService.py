"""
    @name - UpdateObjectService
    @description - Servicio para actualizar un objeto por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.service.IService import IService
from src.service.type_object.FindByIdTypeObjectService import FindByIdTypeObjectService
from src.service.subobject.FindByIdSubObjectService import FindByIdSubObjectService

from src.feign.AuditFeign import AuditFeign

from src.model.entity.Object import Object

from src.persistence.repository.object.UpdateObjectRepository import UpdateObjectRepository
from src.persistence.schema.ObjectSchema import ObjectSchema

from src.util.constant import RESPONSE
from src.util.constant import FEIGN
from src.util.constant import DATABASE
from src.util.common_feign import feign_audit_save, feign_audit_save_error, feign_audit_build_error

class UpdateObjectService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = UpdateObjectRepository(db)
        self.schema:ObjectSchema = ObjectSchema()
        self.find_by_id_type_object = FindByIdTypeObjectService(db)
        self.find_by_id_subobject = FindByIdSubObjectService(db)
        # Comunicacion con el servicio auditoria
        self.feign_audit = AuditFeign("FEIGN_ARCEN")
        # Servicio y operacion actual
        self.current_service = FEIGN['type']['service']['object']
        self.current_operation = FEIGN['type']['generic']['put']['update']

    # @override
    # @method - Actualizar un objeto por su pk
    # @parameter - data - Json con el objeto a actualizar
    # @return - Object
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
                RESPONSE['object']['put']['update']['error']['default']
            )
        feign_audit_save(
            self.feign_audit,
            self.current_service,
            self.current_operation,
            element
        )
        return element
    
    # @method - Verifica la depedencia del objecto
    # @parameter - data - Json con el objeto a validar
    # @return - list
    def dependence(self, data):
        object:Object = Object(**dict(data[DATABASE['table']['object']['name']]))
        # Se consulta el tipo de objeto
        type_object = self.find_by_id_type_object.execute(dict({
            DATABASE['table']['type_object']['pk']: object.id_type_object
        }))
        # Se consulta el subobjeto
        subobject= self.find_by_id_subobject.execute(dict({
            DATABASE['table']['subobject']['pk']: object.id_sub_object
        }))
        return [type_object, subobject]
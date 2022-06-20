from src.feign.AuditFeign import AuditFeign

from src.util.constant import UTIL
from src.util.common import find_env
from src.util.common import convert_json
from src.util.common import get_exception_http

##########################################################
# FEIGN  
##########################################################

# @method - Registra la auditoria
# @parameter - feign_audit - Conexion al microservicio auditoria
# @parameter - response - Respuesta del servicio
# @return - Audit
def feign_audit_save(feign_audit:AuditFeign, service, operation, response):
    response = convert_json(response)
    env = find_env("FEIGN_ARCEN_SAVE")
    audit = feign_audit.build(service, operation, response)
    return feign_audit.save(env, audit)
    
# @method - Registra la auditoria con error
# @parameter - response - Respuesta del servicio
# @return - Audit
def feign_audit_save_error(feign_audit:AuditFeign, service, operation, error):
    name_code = UTIL['format']['response'][0]
    name_msg = UTIL['format']['response'][1]
    feign_audit_save(feign_audit, service, operation, {
        name_code: error[name_code],
        name_msg: error[name_msg]
    })
    raise get_exception_http(error)

# @method - Construye el mensaje de error de la auditoria
# @parameter - code - Representa el codigo error
# @parameter - name_msg - Representa el mensaje de error
# @return - Document
def feign_audit_build_error(code, error):
    name_code = UTIL['format']['response'][0]
    name_msg = UTIL['format']['response'][1]
    return dict({
        name_code:code,
        name_msg: error
    })
    
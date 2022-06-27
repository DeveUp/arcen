"""
    @name - UpdateUserRouter
    @description - Punto de entrada servicio user operacion actualizar el estadoLogin de un user por su email
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.LoginDto import LoginDto
from src.model.response.UserResponse import UserResponse as ResponseArcen
from src.service.login.LoginUserService import LoginUserService as ServiceArcen
from src.persistence.database.table.UserTable import UserTable as TableArcen
from src.util.constant import COLUMN_USER, ENDPOINT_APP, ENDPOINT_APP_LOGIN
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_LOGIN

router_login_user = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_LOGIN
response = ResponseArcen
status = RESPONSE_STATUS_CODE_GENERIC_LOGIN

# @Rest - Actualiza un user por su email
# @Parameter - endpoint - Representa el punto de entrada
# @Parameter - response_model (Optional) - Representa el objeto de respuesta
# @Parameter - status_code (Optional) - Representa el codigo de respuesta
# @Return - Response<User>
@router_login_user.post(endpoint, response_model = response, status_code= status,tags=["UserLogin"])
async def save(user: LoginDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_USER: user})
    service = ServiceArcen(db)
    return service.execute(data)
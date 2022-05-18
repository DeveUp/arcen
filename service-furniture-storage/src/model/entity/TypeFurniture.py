import datetime as _dt
import sqlalchemy as _sql

import src.persistence.database.database as _database
from src.util.constant import DATABASE_POSTGRESQL_TABLE_TYPE_FURNITURE

class TypeFurniture(_database.Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_TYPE_FURNITURE
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    number_type_furniture = _sql.Column(_sql.String, index=True)
    count_rack = _sql.Column(_sql.Integer, index=True)
    count_row = _sql.Column(_sql.Integer, index=True)
    depth = _sql.Column(_sql.Integer, index=True)
    height = _sql.Column(_sql.Integer, index=True)
    width = _sql.Column(_sql.Integer, index=True)
    date= _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
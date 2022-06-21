"""
    @name - database
    @description - Conexion a la base de datos
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.util.common import find_env

engine = create_engine(find_env("POSTGRESQL_CONNSTRING"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

"""
    @name - IRepository
    @description - Interfaz para los repositorios
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from abc import ABCMeta, abstractmethod

class IRepository:
    __metaclass__ = ABCMeta

    # @method - Implementacion funcion a ejecutar
    # @parameter - Json con la informacion del repositorio
    # @return Generic
    # @exception NotImplementedError
    @abstractmethod
    def execute(self, data:dict): raise NotImplementedError
"""
    @name - ITable
    @description - Interfaz tabla de la base de datos
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from abc import ABCMeta, abstractmethod

class ITable:
    __metaclass__ = ABCMeta

    # @method - Implementacion funcion a ejecutar
    # @return Generic
    # @exception NotImplementedError
    @abstractmethod
    def execute(self): raise NotImplementedError
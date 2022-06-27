"""
    @name - ITable
    @description - Interfaz tabla de la base de datos
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from abc import ABCMeta, abstractmethod

class ITable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self): raise NotImplementedError
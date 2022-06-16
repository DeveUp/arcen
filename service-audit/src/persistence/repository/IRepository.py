from abc import ABCMeta, abstractmethod

# @Interface IRepository
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class IRepository:
    __metaclass__ = ABCMeta

    # @Method - Implementacion
    # @Parameter - data - Informacion generica
    # @Return Generic
    # @Exception NotImplementedError
    @abstractmethod
    def execute(self, data:dict): raise NotImplementedError
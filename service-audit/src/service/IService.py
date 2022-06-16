from abc import ABCMeta, abstractmethod

# @Interface IService
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class IService:
    __metaclass__ = ABCMeta

    # @Method - Implementacion
    # @Parameter - data - Informacion generica
    # @Return Generic
    # @Exception NotImplementedError
    @abstractmethod
    def execute(self, data:dict): raise NotImplementedError
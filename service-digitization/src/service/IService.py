from abc import ABCMeta, abstractmethod

class IService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, data:dict): raise NotImplementedError
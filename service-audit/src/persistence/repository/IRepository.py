from abc import ABCMeta, abstractmethod

class IRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, data:dict): raise NotImplementedError
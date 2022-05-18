from abc import ABCMeta, abstractmethod

class ITable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self): raise NotImplementedError
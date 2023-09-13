from abc import ABCMeta, abstractmethod

class Run(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'run') and 
                callable(subclass.run) or 
                NotImplemented)


    @abstractmethod
    def run(self):
        raise NotImplementedError
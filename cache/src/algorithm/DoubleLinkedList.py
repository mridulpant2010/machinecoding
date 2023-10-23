import abc

class DoubleLinkedList(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def insertAtEnd():
        pass
    
    @abc.abstractmethod
    def removeAtBeginning():
        pass
    
    @abc.abstractmethod
    def linkedListSize():
        pass
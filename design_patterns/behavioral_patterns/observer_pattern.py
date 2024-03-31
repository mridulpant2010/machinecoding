from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from random import randint


  
class Subject(ABC):
  @abstractmethod
  def attach(self,observer: Observer):
    pass
  
  @abstractmethod
  def detach(self,observer: Observer):
    pass
  
  @abstractmethod
  def notify(self,observer: Observer):
    pass
  
  @abstractmethod
  def some_business_logic(self,observer: Observer):
    pass

class Observer(ABC):
  @abstractmethod
  def update(self,subject: Subject):
    pass

class ConcreteObserver1(Observer):
  def update(self,subject: Subject):
    return "Concrete Observer1 updates"

class ConcreteObserver2(Observer):
  def update(self,subject: Subject):
    return "Concrete Observer2 updates"
    
class ConcreteSubject(Subject):
  _state:int =None
  _observers: List[Observer] = []
  def attach(self,observer: Observer):
    self._observers.append(observer)
  def detach(self,observer: Observer):
    self._observers.remove(observer)
  def notify(self,observer: Observer):
    for each_l in self._observers:
      each_l.update(self)
  def some_business_logic(self,observer: Observer):
    self._state = randint(1,3)
    self.notify(observer)


def main():
  subscriber: Observer = ConcreteObserver1()
  publisher: Subject  = ConcreteSubject()
  publisher.attach(subscriber)
  publisher.some_business_logic(subscriber)
  publisher.detach(subscriber)
    
    
    

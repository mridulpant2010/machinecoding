from abc import ABC, abstractmethod
from typing import List
from __future__ import annotations
from random import randint

class Observer(ABC):
  @abstractmethod
  def update(subject:Subject):
    pass

class ConcreteObserver1(Observer):
  def update(subject:Subject):
    return "Concrete Observer1 updates"

class ConcreteObserver2(Observer):
  def update(subject:Subject):
    return "Concrete Observer2 updates"
  
class Subject(ABC):
  @abstractmethod
  def attach(observer:Observer):
    pass
  
  @abstractmethod
  def detach(observer:Observer):
    pass
  
  @abstractmethod
  def notify(observer:Observer):
    pass
  
  @abstractmethod
  def some_business_logic(observer:Observer):
    pass


class ConcreteSubject(Subject):
  _state:int =None #but whose state is this?
  _observers: List[Observer] = []
  def attach(observer: Observer):
    self._observers.append(observer)
  def detach(observer:Observer):
    self._observers.remove(observer)
  def notify(observer:Observer):
    for each_l in self._observers:
      each_l.update(self)
  def some_business_logic(observer:Observer):
    self._state = randint(1,3)
    self.notify(observer)


def main():
  subscriber:Observer = ConcreteObserver1()
  publisher:Subject  = ConcreteSubject()
  publisher.attach(subscriber)
  publisher.some_business_logic(subscriber)
  publisher.detach(subsriber)
    
    
    

'''
There is a vehicle parent class and multiple child classes inherit those methods but let's say child_class_1 and child_class_3 creates same functionality method in them respectively, now the code has become redundant and no more we can scale it properly.
If we have to add more and more methods in those sub-classes and the child subclasses have the same repeated methods it will again create redundancy and won't scale because of that.
'''
from abc import ABC, abstractmethod

class Vehicle:
  def __init__(self,drive_method):
    self.drive_method = drive_method
  def drive(self):
    return self.drive_method.drive()

class DriveStrategy(ABC):
  @abstractmethod
  def drive(self):
    pass

class SpecialDrive(DriveStrategy):
  def drive(self):
    return "special drive method"

class NormalDrive(DriveStrategy):
  def drive(self):
    return "normal drive method"


class SportsVehicle(Vehicle):
  def __init__(self):
    super().__init__(SpecialDrive())

class NormalVehicle(Vehicle):
  def __init__(self):
    super().__init__(NormalDrive())

class OffRoadVehicle(Vehicle):
  def __init__(self):
    super().__init__(SpecialDrive())


def main():
  sportsVehicle: Vehicle = SportsVehicle()
  normalVehicle: Vehicle = NormalVehicle()
  offRoadVehicle: Vehicle = OffRoadVehicle()
  sportsVehicle.drive()
  normalVehicle.drive()
  offRoadVehicle.drive()

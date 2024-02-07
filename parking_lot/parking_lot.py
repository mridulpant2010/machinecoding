from datetime import datetime
from collections import list

class Gate:
    
    def __init__(self):
        self.parking_attendant = True
        self.parking_ticket= ParkingTicket()
    
    
    def entry_gate(self,vehicleType):
        #process parkingTicket
        # assign a parking ticket 
        # allocate a spot 
        if self.parking_attendant:
            self.parking_ticket.assignTicket(vehicleType)
            
    def exit_gate(self, ParkingTicket: parkingTicket): 
        #validate payments on the hourlybasis.
        if self.parking_attendant:
            cost = self.parkingTicket.time_validation()
            payment = Payment()
            status = payment.pay(cost)
            if status : 
                sel\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                    
            #vacateSpot
                #how will i vacacte the spots.
                pass
    


class Floor:
    
    def __init__(self,size):
        pass
        self.level = size
        self.gates = list(Gate)
        self.available_spots = 0
    
    def vacateSpot(self):
        self.available_spots += 1

    def displayBoard(self):
        return self.available_spots
    
    def allocateSpot(self,vehicleType):
        if vehicleType == Vehicle.Motorcycle:
            cost +=10
        elif vehicleType == Vehicle.Car:
            cost +=20
        else:
            cost += 30
        self.available_spots -= 1
    
# class ParkingSpot:
#     pass

class ParkingLot:
    #multiple floors in the parking lot.
    # should be multiple gates 
    
    def __init__(self,num_level):
        self.levels = num_level
        self.floor = Floor(num_level)
        self.available_spots= None
    
    def allocate(self,vehicleType):
        self.available_spots = self.floor.allocate_spot(vehicleType)
        if self.available_spots :
            pass
            
    

class Vehicle(enum):
    Motorcycle 
    Car
    Bus
    

class ParkingTicket:
    def __init__(self,vehicleType):
        self.vehicleType = vehicleType
        #self.startTime = startTime
        self.cost = 0
        
    
    def assignTicket(self):
        self.startTime = datetime.now()
        if self.vehicleType == Vehicle.Motorcycle:
            self.cost +=10
        elif self.vehicleType == Vehicle.Car:
            self.cost +=20
        else:
            self.cost += 30
            
    def time_validation(self):
        currenTime = datetime.now()
        numberofHours = (currentTime-self.startTime)//60
        if numberofHours >=1:
            self.cost = numberofHours*self.cost
        return self.cost
    
    
class Payment:
    
    def pay(self):
        if not success:
            return False
        return True
        

class PaymentType(Enum):
    UPI
    Cash
    CreditCard

#main thing is to define the relationship
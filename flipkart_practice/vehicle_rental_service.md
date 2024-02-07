VEHICLE RENTAL SERVICE

Description:
Flipkart is starting a new vehicle rental service Flipkar. In this service, we will rent different kinds of vehicles such as cars and bikes.

Features:
Rental service have multiple branches throughout the city. Assume one city for now.
Each branch has limited number of different kinds of vehicles.
Each vehicle can be booked with predefined price. For simplicity, assume fixed pricing.
Each vehicle can be booked in multiples of 1 hour slot each. (For simplicity, assume slots of single day)
No past bookings should be allowed.

Requirements:
Onboard a new branch with available vehicle
Onboard new vehicle(s) of existing type to a particular branch
Rent vehicle for a time slot and a vehicle type(lowest price as the default choice extendable to any other strategy).
Display available vehicles for a given branch

Test Cases:
(Test cases are defined for understanding feature requirements only. Please model it appropriately based on your service implementation)

add_branch(‘gachibowli’, [“1 suv for Rs.12 per hour”, “3 sedan for Rs.10 per hour”, “3 bikes for Rs.20 per hour”]);
add_branch(‘kukatpally’, [“3 sedan for Rs.11 per hour”, “3 bikes for Rs.30 per hour”, “4 hatch_back for Rs.8 per hour”]);
add_branch(‘miyapur’, [“1 suv for Rs.11 per hour”, “10 bikes for Rs.3 per hour”, “3 sedan for Rs.10 per hour”]);
add_vehicle(“gachibowli”, “1 sedan”)
rent_vehicle(‘suv’, 20th Feb 10:00PM, 20th Feb 12:00PM) // return booked from miyapur
rent_vehicle(‘suv’, 20th Feb 10:00PM, 20th Feb 12:00PM) //return booked from gachibowli
rent_vehicle(‘suv’, 20th Feb 10:00PM, 20th Feb 12:00PM) // return - No availability
get_available_vehicles(‘gachibowli’, time range)
3 ‘sedan’ available for Rs 10
3 bikes available for Rs 20

print_system_view(20th Feb 11:00PM, 20th Feb 12:00PM)
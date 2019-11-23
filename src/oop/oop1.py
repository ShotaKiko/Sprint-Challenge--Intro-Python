# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Vehicle:
    #Base Class
    ##def __init__(self, base_variable_name, etc ) so on for each variable
    pass

class GroundVehicle(Vehicle):
    #would have some variables that will be passed to car and motorcycle according to heirarchy provided
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

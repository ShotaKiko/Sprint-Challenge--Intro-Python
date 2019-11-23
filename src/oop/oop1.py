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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2D Movement~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Vehicle:
    #Base Class
    ##def __init__(self, base_variable_name, etc ) so on for each variable
    pass

class GroundVehicle(Vehicle):
    #Subtype class
    pass

class Car(GroundVehicle):
    #subtype from Ground vehicle subclass
    pass

class Motorcycle(GroundVehicle):
    #subtype from Ground vehicle subclass
    pass
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3D potentially 4D movement (if the starship can approach a black hole and experience that time dilation effect or engage in faster than light travel)
class FlightVehicle(Vehicle):
    #Subtype class
    pass

class Starship(FlightVehicle):
    #subtype from flight vehicle subclass
    pass

class Airplane(FlightVehicle):
    #subtype from flight vehicle subclass
    pass
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
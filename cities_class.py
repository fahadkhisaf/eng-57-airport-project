from class_plane import *

class City(Plane):
    def __init__(self, plane_model, airline_name,flight_no, capacity, destination, flight_time):
        super().__init__(plane_model, airline_name, flight_no, capacity)
        self.destination = destination
        self.flight_time = flight_time



## set departure time and arrival time
## use that to calculate flight time

#fly = ("Air bus A380",200,"Istanbul", "4 hours" )
#print(fly)
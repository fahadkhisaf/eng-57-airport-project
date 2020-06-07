from cities_class import *

class Flighttrip(City):
    def __init__(self,plane_model, airline_name,flight_no, capacity, destination, flight_time, flight_date, available_seats):
        super().__init__(plane_model, airline_name,flight_no, capacity, destination, flight_time)
        self.flight_date = flight_date
        self.available_seats = available_seats

    def
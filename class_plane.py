

class Plane:
    def __init__(self, plane_model, airline_name, flight_no, capacity):
        self.plane_model = plane_model
        self.airline_name = airline_name
        self.__flight_no = flight_no
        self.capacity = capacity


    def get_flight_no(self):
        return self.__flight_no

    def set_flight_no(self, flight_no):
        self.__flight_no = flight_no





## Add speed to attributes
#plane = ("Air bus A380", 200)
#print(plane)
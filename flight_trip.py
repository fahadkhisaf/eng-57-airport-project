from class_plane import *

class Flight(Plane):
    def __init__(self,plane_model, airline_name,flight_no, capacity, destination, flight_time, flight_date, available_seats, manifest = None):
        super().__init__(plane_model, airline_name,flight_no, capacity)
        self.destination = destination
        self.flight_time = flight_time
        self.flight_time = flight_date
        self.flight_date = flight_date
        self.available_seats = available_seats
        self.manifest = manifest

    def delay(self, new_time):
        self.departure = new_time

    def divert(self, new_destination):
        self.destination = new_destination

    def alter_aircraft(self, new_plane):
        self.plane = new_plane

    def show_report(self):
        report = vars(self)
        for key, value in report.items():
            print(key.capitalize(), ": ", value)

    def append_manifest(self, passenger):
        self.manifest.append(passenger)

    def show_manifest(self):
        print(f"\nManifest for personnel on flight {self.flight}: ")
        for person in self.manifest:
            print(vars(person))
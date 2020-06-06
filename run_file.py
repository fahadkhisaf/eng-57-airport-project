from class_plane import *
from cities_class import *
from class_staff import *

flight = City("Air bus A380","Turkish Airlines", 788671 ,200,"Istanbul", "4 hours")
employee = Staff("James Bond","British Airway","Pilot","07/07/1982", "707", "British")


#Flight test
#print(flight.plane_model)
# pass
#print(flight.capacity)
# pass
#print(flight.airline_name)
# pass
#print(flight.destination)
# pass
#print(flight.flight_time)
# pass
#print(flight.get_flight_no())
# pass

#Staff test
print(employee.get_full_name())
#pass
print(employee.get_airline_with())
#pass
print(employee.get_tax_no())
#pass
print(employee.get_nationality())
#pass
print(employee.get_dob())
#pass




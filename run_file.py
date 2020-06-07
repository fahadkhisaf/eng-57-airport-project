from class_staff import *
from people import *
from passenger import *
from class_plane import *
from flight_trip import *

flight = City("Air bus A380","Turkish Airlines", 788671 ,200,"Istanbul", "4 hours")
employee1 = Staff("James Smith", "British Airway", "Pilot", "07/07/1982", 707, "British", 110000)
employee2 = Staff("Sarah Davis", "British Airways", "Cabin crew","04/11/1992",876,"American",45000)


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
print(employee1.get_full_name())
#pass
print(employee1.get_airline_with())
#pass
print(employee1.get_tax_no())
#pass
print(employee1.get_nationality())
#pass
print(employee1.get_dob())
#pass
print((employee1.get_salary()))




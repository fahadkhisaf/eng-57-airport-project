from people import  *

class Staff(People):
    def __init__(self,full_name, tax_no, over_18,airline_with, role ,dob,nationality, salary):
        super().__init__(full_name, tax_no, over_18)
        self.__airline_with = airline_with
        self.__role = role
        self.__dob = dob
        self.__nationality = nationality
        self.__salary = int(salary)

    def get_airline_with(self):
        return self.airline_with

    def get_role(self):
        return self.__role

    def get_dob(self):
        return self.__dob

    def get_nationality(self):
        return self.__nationality

    def get_salary(self):
        return self.__salary


#employee = Staff("Fahad Khisas", 788671, True, "British Airways", "Pilot", "07/08/75", "British", 120000)
#print(employee.get_full_name())
#print(employee.get_salary())
#print(employee.over_18)
# all passed







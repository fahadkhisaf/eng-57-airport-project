

class Staff:
    def __init__(self, full_name='',airline_with, role ,dob, tax_no='',nationality):
        self.__full_name = full_name
        self.airline_with = airline_with
        self.role = role
        self.__dob = dob
        self.__tax_no = tax_no
        self.__nationality = nationality

    def get_full_name(self):
        return self.__full_name

    def set_full_name(self):
        return self.__full_name

    def get_airline_with(self):
        return self.airline_with

    def set_airline_with(self):
        return self.airline_with

    def get_dob(self):
        return self.__dob

    def set_dob(self):
        return self.__dob

    def get_tax_no(self):
        return self.__tax_no

    def set_tax_no(self):
        return self.__tax_no

    def set_nationality(self):
        return self.__nationality

    def get_nationality(self):
        return self.__nationality









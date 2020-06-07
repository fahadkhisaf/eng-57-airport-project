from people import *

class Passenger(People):
    def __init__(self, full_name, tax_no, over_18, dob, passport_no, ticket_class = None,ticket_price = None):
        super().__init__(full_name, tax_no, over_18)
        self.__dob = dob
        self.__passport_no = passport_no
        self.ticket_class = ticket_class
        self.ticket_price = ticket_price

    def purchase_ticket(self,ticket_class):
        if ticket_class == "First Class":
            self.ticket_class = "First Class"
            self.ticket_price = 1000
            return "First Class"

        elif ticket_class == "Business Class":
            self.ticket_class = "Business Class"
            self.ticket_price = 750
            return "Business Class"

        elif ticket_class == "Economy":
            self.ticket_class = "Economy"
            self.ticket_price = 300
            return "Economy"

        elif ticket_class == "Infant":
            self.ticket_class = "Infant"
            self.ticket_price = 0
            return "Infant"

    def get_dob(self):
        return self.__dob

    def get_passport_no(self):
        return self.__passport_no

    def set_passport_no(self, passport_no):
        self.__passport_no = passport_no
        passenger_name = self.get_full_name()
        print(f"{passenger_name}, Your name has been added.\n Passport Number: {self.passport_no}")

    def get_ticket_class(self):
        print(f"{self.ticket_class} ticket, price: {self.ticket_price}")

    def set_ticket_type(self, new_ticket):
        self.ticket_class = new_ticket
        passenger_name = self.get_full_name()
        print(f"Ticket type updated for passenger: {passenger_name},\n Ticket class :{self.ticket_class}")


#passenger1 = Passenger("Christian Bale",768777, True,"02/07/82","7888675GB")
#print(passenger1.get_full_name())
#passenger1.set_ticket_type("First Class")
#passenger1.set_ticket_type("Economy"))

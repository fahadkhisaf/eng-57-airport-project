class People:
     def __init__(self, full_name, tax_no, over_18 = True):
         self.__full_name = full_name
         self.__tax_no = tax_no
         self.over_18 = over_18

     def get_full_name(self):
         return self.__full_name

     def set_full_name(self, full_name):
         self.__full_name = full_name

     def get_tax_no(self):
         return self.__tax_no

     def set_tax_no(self, tax_no):
         self.__tax_no = tax_no

#person = People("Fahad Khisaf", 788671, True)
#print(person.get_full_name())
#print(person.over_18)
#print(person.get_tax_no())



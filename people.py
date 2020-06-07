class People:
     def __init__(self, full_name='', tax_no='', over_18 = True or False):
         self.__full_name = full_name
         self.__tax_no = tax_no
         self.over_18 = over_18

     def get_full_name(self):
         return self.__full_name.title()

     def get_tax_no(self):
         return self.__tax_no

     def get_over_18(self):
         return self.over_18



#person = People("fahad khisaf", 788671, True)
#print(person.get_full_name())
#print(person.over_18)
#print(person.get_tax_no())
# all pass



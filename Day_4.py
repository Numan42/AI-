# OPP concept
class Person:
    def __init__(self, user_name, email, pasoword, address):
        self.user_name = user_name
        self.email = email
        self.password = pasoword
        self.Address = address
        
    def greet(self):
        print(f"{self.user_name} welcome")
    
    def person_address(self):
        print(f"address of {self.user_name} is {self.Address}")
    

person_1 = Person("numan","itsnuman@gmail.com",111111,"west london")
        
person_1.greet()
person_1.person_address()
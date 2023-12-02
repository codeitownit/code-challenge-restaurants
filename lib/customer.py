class Customer:
    def __init__(self, first_name="George", last_name="Washington"):
        self.first_name = first_name
        self.last_name = last_name
    def given_name(self):
        return self.first_name
    def family_name(self):
        return self.last_name


customer1 = Customer("Eve", "Gachui") 
print(customer1.first_name)
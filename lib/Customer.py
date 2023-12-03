class Customer:
    all_customers = []


    def __init__(self, first_name="George", last_name="Washington"):
        self.first_name = first_name
        self.last_name = last_name
        Customer.all_customers.append(self)

    def given_name(self):
        return self.first_name
    def family_name(self):
        return self.last_name
    def full_name(self):
        return f"{self.first_name}" + " "+f"{self.last_name}"
    
    @classmethod
    def all(cls):
        return cls.all_customers


customer1 = Customer("Eve", "Gachui") 
customer2 = Customer("Bruno", "Gachui")

# Getting all customers
all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name())



from lib.Review import Review


class Restaurant(Review):
    all_restaurants = []

    def __init__(self, name):
        self._name = name
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def reviews(self):
        return [review for review in Review.all_reviews if review.restaurant == self]

    name = property(get_name, set_name,)

restaurant1 = Restaurant("Sample Restaurant")
print(restaurant1.reviews())
# print(restaurant1.get_name()) 
# print(restaurant1.reviews())


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



class Restaurant:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
restaurant1 = Restaurant("Sample Restaurant")


class Review:
    all_reviews = []  # Class variable to store all instances of Review

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        # Adding the instance to the class variable
        Review.all_reviews.append(self)

    def get_rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews

# Example usage:
# Assuming you have a Customer instance (customer1) and a Restaurant instance (restaurant1)

# Creating reviews
review1 = Review(customer1, restaurant1, 4.5)
review2 = Review(customer2, restaurant1, 3.8)

# Getting the ratings for reviews
print(review1.get_rating())  # Output: 4.5
print(review2.get_rating())  # Output: 3.8

# Getting all reviews
all_reviews = Review.all()
for review in all_reviews:
    print(f"Rating by {review.customer.full_name()} for {review.restaurant.get_name()}: {review.get_rating()}")

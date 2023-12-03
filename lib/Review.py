from Customer import Customer
class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews
    
    # Create some customer and restaurant instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")
restaurant1 = "Restaurant A"
restaurant2 = "Restaurant B"

# Create some reviews
review1 = Review(customer1, restaurant1, 4.5)
review2 = Review(customer2, restaurant2, 3.7)

# Test instance methods
print(review1.customer())  # Output: John Doe
print(review1.restaurant())  # Output: Restaurant A

# Test class method
all_reviews = Review.all()
for review in all_reviews:
    print(review.customer().get_full_name(), review.restaurant(), review.rating)

# Output:
# John Doe Restaurant A 4.5
# Jane Smith Restaurant B 3.7
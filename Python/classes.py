# Read this blog for better understanding : https://medium.com/@mogheshwetha15/never-forget-again-understanding-classes-objects-methods-in-python-part-1-d8db8f22f27f

# Create a book class for displaying bookdetails
class Book:
  def __init__(self, name, author):
    # attributes
    self.name = name
    self.author = author
  # method
  def bookdetail(self):
    print(f"{self.author} is the author of {self.name}")

# Create book object
book = Book('Black matter','Blake Crouch')
# Apply the method on created object
book.bookdetail()


# Create a house class for displaying house details(methods) for different house object
class House:
    def __init__(self, bedrooms, bathrooms, color):
        # attributes
        self.bedrooms = bedrooms  # Number of bedrooms
        self.bathrooms = bathrooms  # Number of bathrooms
        self.color = color  # Color of the house
    
    # methods
    def open_door(self):
        print("The door is open.")

    def turn_on_lights(self):
        print("The lights are on.")

# Creating a house object from the blueprint (class)
my_house = House(3, 2, "white")
# The real house has attributes (features) and can perform methods (actions)
print(f"My house has {my_house.bedrooms} bedrooms and is painted {my_house.color}.")
my_house.open_door()  # Output: The door is open.
my_house.turn_on_lights()  # Output: The lights are on.

# Creating another house object
my_friend_house = House(3, 3, "yellow")
print(f"My friend;s house has {my_friend_house.bathrooms} bathrooms and is painted {my_friend_house.color}.")
my_friend_house.open_door() 
my_friend_house.turn_on_lights()

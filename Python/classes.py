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


# class House:
#     def __init__(self, rooms, color):
#         # The __init__ method sets the initial attributes for each house instance
#         self.rooms = rooms  # 'self.rooms' is set to the number of rooms for this specific house
#         self.color = color  # 'self.color' is set to the color for this specific house

#     def describe(self):
#         # The describe method uses 'self' to refer to the specific house instance's data
#         print(f'This house has {self.rooms} rooms and is painted {self.color}.')

#     def renovate(self, new_color):
#         # The renovate method uses 'self' to update the color of the specific house instance
#         self.color = new_color  # Update the color of the house
#         print(f'The house has been renovated and is now painted {self.color}.')

# # Building two houses
# house1 = House(3, "blue")  # __init__ sets house1's rooms to 3 and color to "blue"
# house2 = House(4, "red")   # __init__ sets house2's rooms to 4 and color to "red"

# # Describing the houses
# house1.describe()  # Output: This house has 3 rooms and is painted blue.
# house2.describe()  # Output: This house has 4 rooms and is painted red.

# # Renovating house1
# house1.renovate("green")   # Updates house1's color to "green"
# house1.describe()  # Output: The house has been renovated and is now painted green.
#                   #         This house has 3 rooms and is painted green.


class Addition:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        z = self.x + self.y
        print(f"Sum of {self.x} and {self.y} is {z}")
        return z  # Returning the sum so it can be used elsewhere

    def multiply(self, factor):
        # Calling the sum method and capturing its return value
        z = self.sum()
        result = z * factor  # Using the returned sum to perform multiplication
        print(f"After multiplying by {factor}, the answer is {result}")

# Creating an instance of the Addition class
calculate1 = Addition(2, 4)
calculate1.sum()         # Output: Sum of 2 and 4 is 6
calculate1.multiply(6)   # Output: After multiplying by 6, the answer is 36


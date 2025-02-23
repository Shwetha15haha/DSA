# 1. A function that prints a greeting message to the user(name)

# Define the function and pass an argument called name
def greetings(name):
    # Greeting message
    print(f"Hello {name}! Welcome to understanding functions in python.")

# Calling the function
greetings("Friends")

# Let's display the greeting message to a different list of users
users_list = ['Phoebe', 'Rachel', 'Monica', 'Ross', 'Joey', 'Chandler']

# Use a for loop to iterate the code for each user in the users list
for user in users_list:
    greetings(user)

# Output :
# Hello Friends! Welcome to understanding functions in python.
# Hello Phoebe! Welcome to understanding functions in python.
# Hello Rachel! Welcome to understanding functions in python.
# Hello Monica! Welcome to understanding functions in python.
# Hello Ross! Welcome to understanding functions in python.
# Hello Joey! Welcome to understanding functions in python.
# Hello Chandler! Welcome to understanding functions in python.

print()

#2. A function that compares two numbers and displays which is greater.

# Define a function to get inputs from user and compare two numbers
def greater_num():
    # If user gives input other than number exception handling message is displayed
    try:
      # Ask user to enter two numbers
      x = float(input("Enter a number: "))
      y = float(input("Enter another number: "))
      print(f"The numbers entered are {x} and {y}")
      # Compare two numbers and print the corresponding message
      if x==y:
          print(f"The numbers entered are equal. Please enter different numbers." )
      elif x>y:
          print(f"The number {x} is greater than {y}" )
      elif y>x:
          print(f"The number {y} is greater than {x}" )
    except ValueError:
        # Handle the case where input is not a valid number
        print("Please eneter a valid number")

greater_num() 
# Output :
# Enter a number: 2
# Enter another number: 2
# The numbers entered are 2.0 and 2.0
# The numbers entered are equal. Please enter different numbers.
greater_num()
# Output :
# Enter a number: 3
# Enter another number: 2
# The numbers entered are 3.0 and 2.0
# The number 3.0 is greater than 2.0
greater_num()
# Output :
# Enter a number: 2
# Enter another number: 3
# The numbers entered are 2.0 and 3.0
# The number 3.0 is greater than 2.0
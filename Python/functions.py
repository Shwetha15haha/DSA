# A function that prints a greeting message to the user(name)

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


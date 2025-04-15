#Define a decorator function to extend the base function
def add_chili_fakes(func):
  def wrapper(*args, **kwargs):
    print("*You add chili flakes*")
    return func(*args, **kwargs)
  return wrapper

@add_chili_fakes
# Define a base function, this will remain same
def get_pizza(size):
  print(f"Here is your {size} size pizza🍕!")
  return f"Enjoy your {size} pizza with chili flakes!"

result=get_pizza('large')
print(result)
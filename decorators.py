# Decorations

# create main_func()
def main_func(func):
  # define second_func(), same as closures
  def second_func():
    print("welcome here") # this will be execute first
    func() # then will execute func() as argument of main_func()
  return second_func

# define other_func()
def another_func():
  print("I am a another function")

# create decorations with this ^_^ , where another_func re-declare
# and first another_func() passed into main_func parameter as argument
another_func = main_func(another_func)

# call it again !!
another_func()

# in other way
@main_func
def other_func():
  print("Yes welcome too")

# call it !!
other_func()


# =============================================================== #
# create another example within parameter

# define smart_times function
def smart_times(func):
  # define inner function with initial a=0 and b=0
  def inner(a=0, b=0):
    # testing print a and b to know values of each variables
    print("a is {}".format(a))
    print("b is {}".format(b))
    return func(a,b)
  return inner

# create smart_times as decorator
@smart_times
def times(a, b):
  return ("a times b equal to: {}".format(a*b))

# call times with no argument
print(times())
# call times with argument a=10
print(times(a=10))
# call times with argument b=5
print(times(b=5))
# call times with args a=5, b=5. so a*b = 25
print(times(5,5))


# ========================================================== #

# Chain Decorations

def percent(func):
  def inner(*args,**kwargs):
    print("%"*30)
    func(*args, **kwargs)
    print("%"*30)
  return inner

def start(func):
  def inner(*args, **kwargs):
    print("*"*30)
    func(*args, **kwargs)
    print("*"*30)
  return inner

@percent
@start
def hello():
  print("Hello World")

hello()

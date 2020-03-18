# python closures example

def main_function(message):
  
  def second_function():
    print(message) # message sebagai non-lokal var

  return second_function


# define another function
another_func = main_function("Hello All")

# call another function
another_func()

# if we delete the main_function
del main_function

# then call another function again, the another function still work and saved the data before

# if we call this function will return an error
# "main_function is not define"
# main_function("hello")

# will still return "Hello All"
another_func()

# its called python closures



# ========================================== #
# more example with argument

# define make_multiplier function
def make_multiplier_of(n):

  def multiplier(x):
    # return x times n
    return x * n 

  return multiplier

# define multiplier_of_10 with n = 10
multiplier_of_10 = make_multiplier_of(10)
# define multiplier_of_5 with n = 5
multiplier_of_5 = make_multiplier_of(5)


# call multiplier_of_10 with x = 5, return 50
print(multiplier_of_10(5))
# call multiplier_of_5 with x = 5, return 25
print(multiplier_of_5(5))
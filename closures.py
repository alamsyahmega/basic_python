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
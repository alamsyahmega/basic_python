def sambutan(nama):
  """
  Fungsi ini digunakan untuk menyambut
  nama yang di passing kedalam parameter 'nama'
  """
  print("Halo {}, Selamat pagi!".format(nama))

# memanggil fungsi
sambutan("Sam")

# Docstring
# berfungsi untuk memberitahukan untuk apa fungsi itu dijalankan
# berada di bawah nama fungsinya
print(sambutan.__doc__)


# ====================================================== #
# function with return statement

def do_multipy(a,b):
  """This function is for multiply a and b
  and will return the result
  """
  return a * b

# call the function
print(do_multipy(10,10))

# ================================================ #
# scope variable

def scope_var():
  x = 10
  print("value inside function: {}".format(x))

x = 20
scope_var()
print("value outside function: %s" %(x))


# ============================================== #
# type of functions
# 1. build-in functions
# 2. user-defined functions

# example
# 1. slice(), sorted(), str(), type(), etc

# sorting ascending
a = [10, 2, 4, 1]
b = sorted(a)
print(b)

# change to string
c = str(a)
print(c, type(c))

# 2. User-defined , example we create function to devide 
def devide(a,b):
  """Function for devide a and b"""
  return a/b # automatically return float type

print(devide(10, 2))

# ================================================ #

# function with argument

def greeting(name,msg):
  """This function greets to
  the person with the provided message"""
  print("Hello {}, {}!".format(name, msg))

greeting("Sam", "Good Evening") # "Sam" and "Good evening" both are arguments

# if we not pass argument, it will return an error
# example
# greeting("sam") # <-- will return error "greeting() missing 1 required positional argument: 'msg'""


# Default argument
def greeting_def_args(name, msg="Good morning!"):
  """
  This function greets to
  the person with the
  provided message.

  If message is not provided,
  it defaults to "Good
  morning!"
  """
  print("Hello %s, %s" %(name,msg))

greeting_def_args("Monica", "Good Night")
greeting_def_args("Monica")
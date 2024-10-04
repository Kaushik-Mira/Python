x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)

# Global Variables
x = "awesome"
def myFunction():
    print('Python is ' + x)
myFunction()

# Global Variables Second Example
x = "awesome"
def myFunction():
    global x
    x = "fantastic"
myFunction()
print('Python is ' + x)

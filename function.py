#from functions import cube
import functions
def square (x):
    return x * x 
for i in range(10):
    print(f"the square of {i} is {square(i)}")
    print(f"the cube of {i} is {functions.cube(i)}")

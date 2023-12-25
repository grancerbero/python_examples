import sys

try:
    x =  int (input("x:"))
    y =  int (input("y:"))
    result  = x / y
    print (f"{x} /  {y} = {result}")
#except ZeroDivisionError:
#    print ("Error: cannot divide by 0.")
#    sys.exit(1)
#except ValueError:
#    print ("Error: Invalid input")*/
except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")




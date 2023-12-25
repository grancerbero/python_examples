def announce (f):
    def wrapper ():
        print ("About to run the funcion ...")
        f()
        print ("Done with the funcion.")
    return wrapper

@announce 
def hello ():
    print ("Hello, world")

hello()
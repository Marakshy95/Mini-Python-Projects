

#functions with default values
# def my_function(a=1, b=2, c=3):
#     print(a + b + c)
# my_function(b=4)



#*args accepts all arguments coming in and uses them to do something
#kind of like unlimited positional arguments!
#* operator collects aall the arguments in a tuple

def add(*args):
    #can call args[0]
    return sum(args)


print(add(1,2,3,4,5,7,8,9,10))


#** kwargs is a way to pass keyword arugments and not positional 
#turns it into a dictionary not a tuple

def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(6, add=3 , multiply=5)






class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")                      # self.make = kw["make"]      
        self.make = kw.get("model")                      # self.make = kw["make"]      
        self.make = kw.get("color")                      # self.make = kw["make"]      
        self.make = kw.get("seats")                      # self.make = kw["make"]      



my_car = Car(make = "nissan", model="gti")   

print(my_car.make)
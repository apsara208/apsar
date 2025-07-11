#class name should start with a capital letter
class Car:
    #__init__(self) /initialize /constructor
    def __init__(self , make , model , year , color):
        #attributes
        self.make =make
        self.model=model
        self.year=year
        self.color=color
    
    #methods
    def drive(self):
        print("this car is driving")
    def stop(self):
        print("this car has stopped")
    def compliment(self):
        print(self.model,"of",self.make,"is a brilliant car")
#self is a conventionally used parameter name that represents the instance of the class
#__init__ is a special method, often referred to as the constructor
#a constructor is a special method used to initialize an object when it is created. It is defined using the __init__ method and is automatically called when an instance of a class is created.
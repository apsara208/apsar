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

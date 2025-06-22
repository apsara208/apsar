#functions-- a block of reusable codes
'''
def hbd():
    print("happy birthday to you!"*2)
    print("may god bless you")

hbd()
hbd()
hbd()'''
# arguments and parameter:
#do not need to specify the datatype of argument

'''
def userdata(name,age, height):
    print(f"you name is {name}, you are {age} years old and your height is {height:.2f}, am i right?")
userdata("Rahul",21,180.4)
# float argument (not in the function def code block)  (amount:.2f) enter para meter upto 2 decimal points
'''







#RETURN : statement used to end a function and send the result to the user

def add(x,y):
    z=x+y 
    return z    
add(3,5) #local variables can be used as a local variable again 
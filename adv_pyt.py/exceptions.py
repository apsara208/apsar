#error and exceptions
#a=5+"10"
#type error

#f=open("somefile.txt")
#file not found

'''x= -5
if x<0:
    raise Exception("x should be positive")'''

'''y=-3
assert (y>=0),"y is not positive"'''
'''except zerodivisonerror at e:
    print(e)
'''
try:
    a=5/0
except:
    print("an error happened")
else:
    print("everything is fine")  #if no exception occurs
finally:
    print("cleaning up")


class ValurTooHighError(Exception):
    print("value is too high")
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message =message
        self.value = value

def test_value(x):
    if x>100:
        raise ValurTooHighError('value is too high')
    if x<5:
        raise ValueTooSmallError("value is too small ", x)
    
try: 
    test_value(200)
except ValurTooHighError as e:
    print(e)
    





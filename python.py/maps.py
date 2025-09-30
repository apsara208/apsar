def make_even(num):
    if num%2==1:
        return num+1
    else:
        return num
x=[22,3,4,2,4,6,7,8,21,225,8,77,5,44]
y=[]
'''
for num in x:
    y.append(make_even(num))
print(y)
'''
y=list(map(make_even,x))
print(y)
#The map() function in Python is a built-in higher-order function that applies a specified function to each item in an iterable (like a list, tuple, or set) and returns a map object (an iterator)
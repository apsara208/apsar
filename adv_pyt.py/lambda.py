#lambda argument: expression
# in one line ..create a fumnction with some argument, evaluate the expression and return the result
add10=lambda x: x+10
print(add10(5))

'''def add10_func(x):
    return x+10'''

mult=lambda x,y:x*y
print(mult(2,7))

points2d=[(1,2,),(15,4),(3,17),(0,-1)]
'''def sort_by_y(x):
    return x[1]
points2d_sorted=sorted(points2d,key=sort_by_y)''' 
points2d_sorted=sorted(points2d,key=lambda x: x[1])
print(points2d)
print(points2d_sorted)
#map :transforms each element with a function 
#map(func,seq)
a=[1,2,3,4,5]
b=map(lambda x:x*2,a)
print(list(b))

c=[x*2 for x in a ] #list comprehension
print(c)

#filter(func,seq)
b=filter(lambda x:x%2==0,a) # can also be done with list comprehension
print(list(b))

#reduce(func,seq)
from functools import reduce
a=(1,2,3,4,5,6)
product_a=reduce(lambda x,y:x*y,a)
print(product_a) #720

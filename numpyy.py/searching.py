import numpy as np
#search
np1=np.array([1,2,4,6,2,8,9,40,4,8,3,3])
x=np.where(np1==3)
print(x) #(array([10, 11]),)
print(x[0]) #[10 11]
print(np1[x[0]]) #[10 11]
#return even items
y=np.where(np1 % 2 == 0)
print(y) #(array([1, 2, 3, 4, 5, 7, 8, 9]),) indexes
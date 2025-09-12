import numpy as np
#slicing numpy arrays
np1=np.array([1,2,3,4,5,6,7])
#return 1,2,3
print(np1[:3])
#return negative slices
print(np1[-3:-1])
#[5, 6]

#steps on entire array
#(every other item)
print(np1[::2])  #[1 3 5 7]

#slicing a 2d array
np2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
#pull out single item
print(np2[1,2])  #8

print(np2[0:1,1:3])    #[row start:not included row,item:item]
#[[2 3]]
print(np2[0:2,1:3])
'''[[2 3]
 [7 8]]'''
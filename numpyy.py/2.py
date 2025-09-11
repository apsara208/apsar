#NumPy is a powerful Python library primarily used for working with arrays. It is the fundamental package for scientific computing in Python, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
import numpy as np

#Numpy= numeric python
#datatype-ndarray=n_dimensional array

np1=np.array([0,1,2,3,4,5,6,7,8,9])
print(np1) #[0 1 2 3 4 5 6 7 8 9]
print(np1.shape) #(10,)

#Range
np2=np.arange(10) 
print(np2) #[0 1 2 3 4 5 6 7 8 9]
#Step
np3=np.arange(1,10,2)
print(np3) #[1 3 5 7 9]
#zeros
print(np.zeros(10)) #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

#Multidimensional
print(np.zeros((2,10)))
'''[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]'''

#full
np4=np.full((10),6)
print(np4) #[6 6 6 6 6 6 6 6 6 6]

#multidimensional full
np5=np.full((2,10),6)
print(np5)
'''[[6 6 6 6 6 6 6 6 6 6]
 [6 6 6 6 6 6 6 6 6 6]]'''

#convert python list to array
my_list=[1,2,3,4,5]
np6=np.array(my_list)
print(np6)
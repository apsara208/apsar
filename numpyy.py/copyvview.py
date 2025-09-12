import numpy as np
#copy vs view
np1=np.array([1,2,3,4,5])
#create and view
np2=np1.view()
print(f'original np1 {np1}')
print(f'original np2 {np2}')
np1[0]=41
print(f'changed np1 {np1}')
print(f'original np2 {np2}')
np2[0]=1
print(f'original np1 {np1}')
print(f'original np2 {np2}')
'''original np1 [1 2 3 4 5]
original np2 [1 2 3 4 5]
changed np1 [41  2  3  4  5]
original np2 [41  2  3  4  5]
original np1 [1 2 3 4 5]
original np2 [1 2 3 4 5]'''
#view shares memory : chaneg in the view list will also affect the original


#copy
np3=np1.copy()
print(f'copied np1 {np3}')
np3[0]=9
print(f' np1 {np1}')
print(f' np2 {np2}')
print(f'copied np1 {np3}')
#copies have independent memories
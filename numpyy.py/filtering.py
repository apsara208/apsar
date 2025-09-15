import numpy as np
#filtering numpy arays with boolean index lists
np1=np.array([1,2,3,4,5,6,7,8,9,0])
'''
x=[True,True,False,False,False,False,False,False,False,False]
print(np1[x])
'''
'''
filtered=[]
for thing in np1:
    if thing %2==0:
        filtered.append(True)
    else:
        filtered.append(False)
print(np1[filtered])
'''
'''ar=[]
for v n np1:
    if v==0 or v==1:
        ar.append(True)
    else:
        ar.append(False)
print(np1[ar])
'''
#shortcut
filtered=np1%2==0
print(np1[filtered])
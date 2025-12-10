import matplotlib.pyplot as plt
import numpy as np
#subplot function can draw multiple plots in one figure
#subplot(rows,cols,which projection)
#plot 1:
x=np.array([0,1,2,4])
y=np.array([9,1,5,7])
plt.subplot(1,2,1)
plt.plot(x,y)

#plot 2 :
x=np.array([0,1,4,5])
y=np.array([4,3,8,10])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.savefig("pics4.png")

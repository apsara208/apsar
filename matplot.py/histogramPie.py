import matplotlib.pyplot as plt
import numpy as np
#histogram : hist()
#A histogram is a graph showing frequency distributions.
#It is a graph showing the number of observations within each given interval.
#For simplicity we use NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10
#(170,10,250)
x=np.random.normal(170,10,250)
plt.subplot(2,1,1)
plt.hist(x)


#pie()
y=np.array([35,25,25,15])
plt.subplot(2,1,2)
plt.pie(y)
plt.savefig("pics7.png")
import matplotlib.pyplot as plt
import numpy as np
#bar(): fuunction is used to draw bar graphs
x=np.array(["A","B","C","D"])
y=np.array([3,4,1,10])
plt.bar(x,y)
plt.savefig("pics6.png")
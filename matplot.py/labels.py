import matplotlib.pyplot as plt
import numpy as np
#labels for x axis and y axis 
#title for the representation 
#fonts for title and labels
#position the title (loc)
#grid(): for grids
a=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
b=np.array([240, 250, 260, 210, 250, 290, 300, 210, 320, 330])
plt.plot(a,b,c="yellow")
font1={"family":"serif","color":"blue","size":20}
font2={"family":"serif","color":"darkred","size":15}
plt.xlabel("average pulse",fontdict=font1)
plt.ylabel("calorie burnage",fontdict=font1)
plt.title("sports watch data",fontdict=font2,loc="left")
plt.grid()
#can add axis="x" or "y", color="" ,linestyle,linewidth inside the braces
plt.savefig("pics3.png")

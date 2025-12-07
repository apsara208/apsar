import pandas as pd
#Pandas uses the plot() method to create diagrams.
#We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
import matplotlib.pyplot as plt
my_df=pd.read_csv("sales.csv")
my_df.plot()
#plt.show()
plt.savefig("plot.png")
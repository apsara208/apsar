import pandas as pd
#Pandas uses the plot() method to create diagrams.
#We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
import matplotlib.pyplot as plt
my_df=pd.read_csv("sales.csv")
#my_df.plot()
#my_df.plot(kind="scatter",x="Sales",y="Expenses")
my_df["Sales"].plot(kind="hist")
#plt.show()

plt.savefig("plot.png")
'''kind value	What it shows
line	Line graph ✅ (default)
bar	Vertical bar chart
barh	Horizontal bar chart
hist	Histogram
box	Box plot
kde	Density curve
area	Area chart
pie	Pie chart
scatter	Scatter plot'''
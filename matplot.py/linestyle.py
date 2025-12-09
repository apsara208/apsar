import matplotlib.pyplot as plt
import numpy as np
y =np.array([3,8,1,10])
plt.plot(y,linestyle='dotted',c="r",linewidth="10") #line,linstyle,linecolor 
plt.savefig("pics2.png")
'''Style	Or
'solid' (default)	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'	
'None'	'' or '''

#linecolor
#(,color=) or (,c=)
#line width (,linewidth)


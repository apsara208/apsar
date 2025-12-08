#Matplotlib is a low level graph plotting library in python that serves as a visualization utility
'''import matplotlib
print(matplotlib.__version__)
'''
import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,6])
y=np.array([0,250])
plt.plot(x,y) #,o : rings no line
plt.savefig("pics.png")
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.savefig("pics.png")
'''o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline'''
 

#formal strings :fmt
#syntax: marker|line|color
#You can also use the shortcut string notation parameter to specify the marker
a=np.array([30,90,45,150])
#marker size =ms ,marker edge color =mec , marker face color = mfc
plt.plot(a,"o:r",ms=20,mec="k",mfc="c")
plt.savefig('pics.png')
'''Line Reference
Line Syntax	Description
'-'	Solid line	
':'	Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line'''

'''Color Reference
Color Syntax	Description
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White	
'''
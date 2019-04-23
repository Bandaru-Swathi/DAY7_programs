import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
m=31
w=[]
for n in range(0,m):
	p=np.cos((2*np.pi*n)/(m-1))
	y=0.5-0.5*p
	w=np.append(w,y)
plt.xlabel('w-axis')
plt.ylabel('y-axis')
#plt.plot(w,y,label="HANNING WINDOW")
plt.stem(w)
plt.show()

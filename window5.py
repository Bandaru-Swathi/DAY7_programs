import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
m=31
w=[]
for n in range(0,m):
	p=np.cos((2*np.pi*n)/(m-1))
	q=0.08*np.cos((4*np.pi*n)/(m-1))
	y=0.42-(0.5*p)+q
	w=np.append(w,y)
plt.xlabel('w-axis')
plt.ylabel('y-axis')
#plt.plot(w,y,label="BLOCKMAN WINDOW")
plt.stem(w)
plt.show()

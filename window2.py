import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
m=31
w=[]
for n in range(0,m):
	p=abs(n-((m-1)*0.5))
	y=1-((2*p)/(m-1))
	w=np.append(w,y)
plt.xlabel('w - axis')
plt.ylabel('y - axis')
#plt.plot(w,y,label = "triangular")
plt.stem(w)
plt.show()

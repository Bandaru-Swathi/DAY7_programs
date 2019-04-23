import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dtft(x):
	j=cm.sqrt(-1)
	y=[]
	n=len(x)
	N=10000
	q=np.linspace(-np.pi,np.pi,N)
	for i in range(0,N):
		w1=q[i]
		sum=0
		for k in range(0,n):
			sum=sum+(x[k]*np.exp(-k*w1*j))
		y.append(sum)
	return y
n=np.arange(-100,100,1)
x1=np.sinc(n*0.25)
x=x1/4
plt.subplot(2,1,1)
plt.stem(n,x,'r')
plt.title('SINC FUNCTION')
t=np.abs(dtft(x))
q=np.linspace(-np.pi,np.pi,10000)
plt.subplot(2,1,2)
plt.plot(q,t)
plt.show()

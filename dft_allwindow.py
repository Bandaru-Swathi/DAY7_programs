import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dft(x):
	N=10000
	j=cm.sqrt(-1)
	y=[]
	n=len(x)
	k=np.linspace(-4000,N-1,N)
	for i in range(0,N):
		sum=0
		for n in range(0,len(x)):
			sum=sum+(x[n]*np.exp((-n*2*np.pi*k[i]*j)/N))
		y.append(sum)
	return y
wh=[]
m=31
for n in range(0,m):
	p=0.5*np.cos((2*np.pi*n)/(m-1))
	y=0.5-p
	wh=np.append(wh,y)
t1=dft(wh)
wt=[]
for n in range(0,m):
	a=2*abs(n-((m-1)*0.5))/(m-1)
	y=1-a
	wt=np.append(wt,y)
w=[]
N=31
for n in range(0,31):
	w1=0.5-(0.46*np.cos((2*np.pi*n)/(N-1)))
	w=np.append(w,w1)
t2=dft(wt)
t3=dft(w)
plt.subplot(6,1,1)
plt.title("dft of hanning window")
plt.plot(t1)
plt.subplot(6,1,2)
plt.title("dft of triangle window")
plt.plot(t2)
plt.subplot(6,1,3)
plt.title("dft of hamming window")
plt.plot(t3)
plt.subplot(6,1,4)
plt.title("hanning window")
plt.plot(wh)
plt.subplot(6,1,5)
plt.title("triangle window")
plt.plot(wt)
plt.subplot(6,1,6)
plt.title("hamming window")
plt.plot(w)		
plt.show()


	

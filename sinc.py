import numpy as np
import matplotlib.pyplot as plt
#import cmath as cm
n=np.arange(0,30,0.1)
x1=np.sinc(n*(np.pi/4))
plt.stem(n,x1/4,'b')
plt.title('SINC FUNCTION')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()

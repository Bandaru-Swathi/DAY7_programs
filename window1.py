import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
x=np.arange(0,31)
y=x/x
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Unit step Graph')
plt.stem(x,y,label = "unitstep")
plt.legend()
plt.show()

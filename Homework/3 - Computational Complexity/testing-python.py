import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,101)

y = -np.cos(x)

plt.plot(x,y)
plt.show()

print("Hello World!")
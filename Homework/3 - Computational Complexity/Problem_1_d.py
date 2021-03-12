import matrixMethods as M
import numpy as np
import matplotlib.pyplot as plt

sizes = [2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]
iterations = 2

tavg_inv = np.zeros(len(sizes))
tavg_imp = np.zeros(len(sizes))

for i in range(1,len(sizes)):

    n = sizes[i]
    print("n = ",n)

    # Getting the average time for the inverse method
    tavg_inv[i] = M.inverseMethod(n,iterations)
    print("Inverse Method: ",tavg_inv[i])

    tavg_imp[i] = M.improvedMethod(n,iterations)
    print("Numpy Linear Algebra Solver Method: ", tavg_imp[i])


# Now we'll plot the result
plt.loglog(sizes,tavg_inv)
plt.loglog(sizes,tavg_imp)
plt.title("Computational Complexity")
plt.xlabel("n")
plt.ylabel("Solution Time (s)")
plt.grid("on")
plt.legend(["Matrix Inversion","Built-in NumPy Solver"])
plt.show()

print("Finite-differencing the last four points in each (in logarithmic space):")
print("Inverse Method Exponent: ",(np.log10(tavg_inv[-1]) - np.log10(tavg_inv[-4])) / (np.log10(8192)-np.log10(1024)))
print("Numpy Method Exponent: ",(np.log10(tavg_imp[-1]) - np.log10(tavg_imp[-4])) / (np.log10(8192)-np.log10(1024)))

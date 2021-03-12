import matrixMethods as M

n = 100
iterations = 1000

# Getting the average time for the inverse method
tavg_inv = M.inverseMethod(n,iterations)
print("Inverse Method: ",tavg_inv)

tavg_imp = M.improvedMethod(n,iterations)
print("Numpy Linear Algebra Solver Method: ", tavg_imp)
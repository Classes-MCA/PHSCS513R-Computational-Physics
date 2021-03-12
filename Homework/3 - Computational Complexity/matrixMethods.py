import time
import numpy as np

def inverseMethod(n,iterations):

    # We will find the time it takes to solve the matrix equation by inverting the matrix A

    t = np.zeros(iterations)
    for i in range(1,iterations): # Do it 1000 times

        A = np.random.randint(-100,100,(n,n))
        b = np.random.randint(-100,100,(n,1))

        tstart = time.time() # Get the start time
        Ainv = np.linalg.inv(A)
        Ainv * b
        tend = time.time()

        t[i] = tend - tstart

    tavg = np.mean(t)
    return tavg

def improvedMethod(n,iterations):

    # We will find the time it takes to solve the matrix equation by using a python solver

    t = np.zeros(iterations)
    for i in range(1,iterations): # Do it 1000 times

        A = np.random.randint(-100,100,(n,n))
        b = np.random.randint(-100,100,(n,1))

        tstart = time.time() # Get the start time
        np.linalg.solve(A,b)
        tend = time.time()

        t[i] = tend - tstart

    tavg = np.mean(t)
    return tavg
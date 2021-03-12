def inverseMethod(n,iterations):

    import time
    import numpy as np

    # We will find the time it takes to solve the matrix equation by inverting the matrix A

    iterations = 1000
    t = np.zeros(iterations)
    for i in range(1,iterations): # Do it 1000 times

        n = 10 # Number of unknowns
        A = np.random.randint(-100,100,(n,n))
        b = np.random.randint(-100,100,(n,1))

        tstart = time.time() # Get the start time
        Ainv = np.linalg.inv(A)
        x = Ainv * b
        tend = time.time()

        t[i] = tend - tstart

    tavg = np.mean(t)
    return tavg
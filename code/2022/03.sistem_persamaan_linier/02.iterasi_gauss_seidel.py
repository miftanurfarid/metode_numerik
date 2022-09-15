import numpy as np

a = np.array([[4, 1, 2, -1],
           [3, 6, -1, 2],
           [2, -1, 5, -3],
           [4, 1, -3, -8]],float)
b = np.array([2, -1, 3, 2], float)
(n,) = np.shape(b)
x = np.full(n, 1, float)
xdiff = np.empty(n, float) # selisih nilai x setiap dua iterasi
iterlimit = 100
tolerance = 1.0e-6

# Iterations
for iteration in range(iterlimit):
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i,j]*x[j]
        xnew = -1/a[i,i] * (s - b[i]) # xnew is scalar
        xdiff[i] = abs(xnew - x[i]) # compute the absolute difference
        x[i] = xnew # assign the new value to x[i]
    print(iteration, "\t", x)
    if (xdiff < tolerance).all(): # check convergence of all equations
        break
    

print('\nJumlah iterasi: %d' % (iteration))
print('Solusi dari sistem:')
print(x)
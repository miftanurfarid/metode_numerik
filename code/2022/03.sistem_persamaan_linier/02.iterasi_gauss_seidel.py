import numpy as np

a = np.array([[8, 1, 3, 2],
           [2, 9, -1, -2],
           [1, 3, 2, -1],
           [1, 0, 6, 4]],float)
b = np.array([0, 1, 2, 3], float)
(n,) = np.shape(b)
x = np.full(n, 0, float)
xdiff = np.empty(n, float) # selisih nilai x setiap dua iterasi
iterlimit = 100
toleransi = 1.0e-6

# iterations
for iterasi in range(iterlimit):
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i,j]*x[j]
        xnew = -1/a[i,i] * (s - b[i]) # xnew is scalar
        xdiff[i] = abs(xnew - x[i]) # compute the absolute difference
        x[i] = xnew # assign the new value to x[i]
    print(iterasi+1, "\t", x)
    if (xdiff < toleransi).all(): # check convergence of all equations
        break
    

print('\nJumlah iterasi: %d' % (iterasi+1))
print('Solusi dari sistem:')
print(x)
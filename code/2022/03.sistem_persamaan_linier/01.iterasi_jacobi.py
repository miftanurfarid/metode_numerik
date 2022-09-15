import numpy as np

a = np.array([[4, 1, 2, -1],
           [3, 6, -1, 2],
           [2, -1, 5, -3],
           [4, 1, -3, -8]],float)

b = np.array([2, -1, 3, 2], float)

(n,) = np.shape(b)
x = np.full(n, 1, float) # tebakan awal = 1.0
xnew = np.empty(n,float)
iterlimit = 100 # jumlah iterasi maksimal
tolerance = 1.0e-6 # derajat akurasi

# iterasi
for iteration in range(iterlimit):
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i,j]*x[j]
        xnew[i] = -1/a[i,i] * (s - b[i])
    print(iteration, "\t", x)
    if (abs(xnew - x) < tolerance).all(): # kondisi konvergen
        break # keluar dari loop
    else:
        x = np.copy(xnew) # copy semua nilai xnew ke x

print('\nJumlah iterasi: %d' % (iteration))
print('Solusi dari sistem:')
print(x)
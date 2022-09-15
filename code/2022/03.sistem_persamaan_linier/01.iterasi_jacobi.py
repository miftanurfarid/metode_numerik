import numpy as np

a = np.array([[8, 1, 3, 2],
           [2, 9, -1, -2],
           [1, 3, 2, -1],
           [1, 0, 6, 4]],float)
b = np.array([0, 1, 2, 3], float)
(n,) = np.shape(b)
x = np.full(n, 0, float) # tebakan awal = 1.0
xnew = np.empty(n,float)
iterlimit = 1000 # jumlah iterasi maksimal
toleransi = 1.0e-6 # derajat akurasi

# iterasi
for iterasi in range(iterlimit):
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i,j]*x[j]
        xnew[i] = -1/a[i,i] * (s - b[i])
    print(iterasi+1, "\t", x)
    if (abs(xnew - x) < toleransi).all(): # kondisi konvergen
        break # keluar dari loop
    else:
        x = np.copy(xnew) # copy semua nilai xnew ke x

print('\nJumlah iterasi: %d' % (iterasi+1))
print('Solusi dari sistem:')
print(x)
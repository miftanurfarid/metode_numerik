# fungsi f(x)
f = lambda x: 2*x**2 - 5*x + 3

# metode secant
def secant(fn, x = list(), tol=1.0E-9, iterasi_maks = 100):
    [x1,x2] = x
    for iterasi in range(iterasi_maks):
        x_baru = x2 - (x2 - x1)/(fn(x2) - fn(x1)) * fn(x2)
        print(iterasi,x_baru) # menampilkan jumlah iterasi dan nilai x
        
        if abs(x_baru - x2) < tol:
            break
        
        x1 = x2
        x2 = x_baru
    else: # else ini milik for-loop
        print('Telah sampai di batas iterasi tanpa menghasilkan solusi')
    return x_baru, iterasi

# memanggil fungsi metode secant
# input x1 dan x2 sebagai python list
x, iterasi = secant(f, [2,3], 0.000001)

# Tampilkan hasil
print(f'\nAkar: {x}')
print(f'Jumlah iterasi: {iterasi}')
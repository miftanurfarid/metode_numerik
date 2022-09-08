def y(x): return 2*x**2 - 5*x + 3 # bentuk persamaan

def rfalsi(fn, x1, x2, tol = 1.0e-6, ilimit = 100): # maksimum 100 iterasi
    y1 = y(x1)
    y2 = y(x2)
    xh = 0
    iterasi = 0
    
    # menghitung titik palsu
    if y1 == 0:
        xh = x1 # jika x1 adalah akar
    elif y2 == 0:
        xh = x2 # jika x2 adalah akar
    elif y1 * y2 > 0: # jika y1 dan y2 memiliki tanda yang sama
        print('Tidak ada akar di dalam interval ini.')
    else:
        for iterasi in range(1,ilimit+1):
            xh = x2 - (x2-x1)/(y2-y1) * y2
            yh = y(xh)
            print(iterasi,xh) # menampilkan jumlah iterasi dan nilai x
            
            if abs(yh) < tol:
                break
            elif y1 * yh < 0: # jika y1 dan yh memiliki tanda berbeda
                x2 = xh
                y2 = yh
            else:
                x1 = xh
                y1 = yh
    return xh, iterasi

# nilai awalan
x1 = 0
x2 = 1.4
x, n = rfalsi(y,x1,x2)

# Tampilkan hasil
print(f'\nAkar: {x}')
print(f'Jumlah iterasi: {n}')
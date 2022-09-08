from sys import exit

# dua nilai awalan x1 dan x2
x1 = 0
x2 = 1.4

y1 = 2*x1**2-5*x1+3
y2 = 2*x2**2-5*x2+3

if y1*y2 > 0: # periksa apakah tandanya sama
    print('Tidak ada akar-akar di dalam interval ini')
    exit() # hentikan program

for iterasi in range(1,101):
    xh = (x1+x2)/2 # hitung nilai tengah
    yh = 2*xh**2-5*xh+3
    y1 = 2*x1**2-5*x1+3
    print(iterasi,x1) # menampilkan jumlah iterasi dan nilai x
    
    if abs(y1) < 1.0e-6:
        break
    elif y1*yh < 0: # periksa perbedaan tanda
        x2 = xh # x1 dan x2 di setengah interval pertama
    else:
        x1 = xh # x1 dan x2 di setengah interval kedua

print(f'\nAkar: {x1}')
print(f'Jumlah iterasi: {iterasi}')
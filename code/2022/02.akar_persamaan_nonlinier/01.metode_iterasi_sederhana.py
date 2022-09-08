x = 0 # nilai awalan

for iterasi in range(1,101): # 100 iterasi
	x_baru = (2*x**2 + 3)/5 # menghitung nilai x_baru
	print(iterasi,x) # menampilkan jumlah iterasi dan nilai x
    
	if abs(x - x_baru) < 0.000001: # tingkat keakuratan
		break # hentikan for-loop
        
	x = x_baru # mendefinisikan nilai x_baru sebagai x
    
print(f'\nAkar: {x_baru}')
print(f'Jumlah iterasi: {iterasi}')

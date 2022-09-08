x = 0 # nilai awalan

for iterasi in range(1,101):
    x_baru = x-(2*x**2-5*x+3)/(4*x-5) # persamaan Newton-Raphson   
    print(iterasi,x) # menampilkan jumlah iterasi dan nilai x	
    
    if abs(x - x_baru) < 0.000001:  # tingkat keakuratan		
        break # hentikan for-loop	
        
    x = x_baru # mendefinisikan nilai x_baru sebagai x
    
print(f'\nAkar: {x_baru}')
print(f'Jumlah iterasi: {iterasi}')
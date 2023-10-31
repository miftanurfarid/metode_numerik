import numpy as np

f  = lambda x: x**2 - 2*x - 3
df = lambda x: 2*x - 2

x1 = 0
eps = 1e-7

print(f"iter. \t x1 \t x2 \t |x2-x1|")
for i in range(100):
    x2 = x1 - f(x1)/df(x1)
    
    print(f"{i+1} \t {np.round(x1,2)} \t {np.round(x2,2)} \t {np.round(abs(x2 - x1),4)}")

    if abs(x2 - x1) <= eps:
        break
    else:
        x1 = x2
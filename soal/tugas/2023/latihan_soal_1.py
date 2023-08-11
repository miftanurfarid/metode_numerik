import numpy as np

f1 = lambda x: -x**2 + 6
f2 = lambda x: np.sqrt(-x+6)

x1 = 0

for i in range(1,10):
    x2 = f2(x1)
    print(f"{i}\t{np.round(x1,4)}\t{np.round(x2,4)}\t{np.round(np.abs(x1-x2),4)}")
    x1=x2
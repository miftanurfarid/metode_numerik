f = lambda x: 0.1 * x ** 5 - 0.2 * x ** 3 + 0.1 * x - 0.2
df = lambda x: 0.5 * x ** 4 - 0.6 * x ** 2 + 0.1
ddf = lambda x: 2 * x ** 3 - 1.2 * x

h = 0.05
x = 0.1
print('Hasil analitik:')
print(f"f({x}) = {f(x)}")
print(f"f'({x}) = {df(x)}")
print(f"f''({x}) = {ddf(x)}")

print('\nHasil numerik')
# Forward differences approximation
dff1 = (f(x+h) - f(x))/h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x))/h**2
print('Forward differences:')
print('f\'(%f) = %f'%(x,dff1))
print('f\'\'(%f) = %f'%(x,dff2))

# Central differences approximation
dfc1 = (f(x+h) - f(x-h))/(2*h)
dfc2 = (f(x+h) - 2*f(x) + f(x-h))/h**2
print('Central differences:')
print('f\'(%f) = %f'%(x,dfc1))
print('f\'\'(%f) = %f'%(x,dfc2))

# Backward differences approximation
dfb1 = (f(x) - f(x-h))/h
dfb2 = (f(x) - 2*f(x-h) + f(x-2*h))/h**2
print('Backward differences:')
print('f\'(%f) = %f'%(x,dfb1))
print('f\'\'(%f) = %f'%(x,dfb2))
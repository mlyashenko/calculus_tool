import sympy as sp

x = sp.Symbol('x')
f = sp.exp(x**2)
print(sp.diff(f, x))
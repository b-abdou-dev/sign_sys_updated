## Orthogonal Expansion using Symbolic Math (sympy)
from sympy import *

# Constants
pi = 3.14
T = 8.500

# defining t as an object (symbol)
t = symbols('t')
f1 = 1 / (2 * T)

# using sympy sinewave
s_1_t = sin(2 * pi * f1 * t)
s_2_t = sin(2 * pi * 2 * f1 * t)
# print(s_1_t)


## implementing and calculating InnerProduct  ∫0T sl(t)s∗ k(t)dt
innerProduct = integrate(s_1_t * conjugate(s_2_t), (t, 0, T))
print(innerProduct)


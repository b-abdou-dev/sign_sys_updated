from cmath import exp, pi
from math import sin
import matplotlib.pyplot as plt

## Given values

# generating sin
sin_vector = []
T = 10
for i in range(0, 100):
    # i = i/10
    sin_vector.append(sin(2*pi*i/T))
x = sin_vector

# - given N as number of samples
N = len(x)
print(N)
# - initialize X vector with Zeros    X_vector= [0 ] *N   with length N

X_vector = []
print(pi)
print(2j)
for k in range(0, N):
    X = 0
    for n in range(0, N):
        X += x[n] * (exp(-2j * pi * k * n) / N)
        print(X)
    X_vector.append(abs(X))
# print(X_vector)


plt.subplot(211)
plt.plot(x)
plt.ylabel('x in Time Domain')


plt.subplot(212)
plt.plot(X_vector)
plt.ylabel('Magnitude in Frequency Domain')
plt.show()

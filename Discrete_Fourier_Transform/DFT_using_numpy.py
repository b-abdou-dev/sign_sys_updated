import numpy as np
import matplotlib.pyplot as plt

## Given values

# generating sin
period = 2*np.pi/5
# w = 2*np.pi/period
w = 20
m = np.linspace(0, 20, 3000)
sin_vector = np.sin(w*m)
x = sin_vector

# - given N as number of samples
N = len(x)
# - initialize X vector with Zeros    X_vector= [0 ] *N   with length N

X_vector = []
def findX():
    for k in range(0, N):
        n = np.linspace(0, N, N)
        omega = (np.pi * k * n) / N
        X = np.sum(x * np.exp(-1j * omega))
        yield abs(X)
X_vector = list(findX())
print(X_vector)
# print(X_vector)

plt.figure(1)
plt.subplot(211)
plt.plot(m, x)
plt.ylabel('Time Domain')


plt.subplot(212)
plt.plot(m*2*np.pi, X_vector)
plt.ylabel('Frequency Domain')
plt.show()

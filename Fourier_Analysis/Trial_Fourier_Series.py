import numpy as np

Pi = 3.14
T = 2 * Pi
x_step = T/1000
x = np.arange(0, T, x_step)
s_of_x = np.sin(2 * Pi * x)    # input signal

# Fourier Coefficients
def a(n):
    return (2 / T) * sum(s_of_x * np.cos(2 * Pi * x * n / T)) * x_step

def b(n):
    return (2 / T) * sum(s_of_x * np.sin(2 * Pi * x * n / T)) * x_step

a0 = (1 / T) * sum(s_of_x) * x_step


# Fourier Series
N = 1000
n_step = 1
n = np.arange(0, N, n_step)
an = a(n)
bn = b(n)
SNx = a0/2 + sum((an * np.cos(2 * Pi * x * n / T)) + (bn * np.sin(2 * Pi * x * n / T)))

print(SNx)
# implement fourier series given (a0, ak, bk , t, )
# Constants of local fourier series function

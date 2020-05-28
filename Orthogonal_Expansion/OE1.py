import numpy as np
import matplotlib.pyplot as plt

# Calculating energy of sinwave signal

pi = np.pi
T=8.500     #  period of sinwave
t_step=1e-3


time = np.arange(0, T, t_step)
f1=1/(2*T) # Frequency of s1(t)
s_1_t=np.sin(2*pi*f1*time) # Sampled vector of s1(t)
s_2_t=np.sin(2*pi*2*f1*time) # Sampled vector of s2(t), has 2f1 frequency


# energy signal of s1t
E1=sum(np.square(abs(s_1_t)))*t_step # Create the energy E1= ∫0T |s1(t)|2dt with numerical integration
print(E1)

# energy signal of s2t
E2=sum(np.square(abs(s_2_t)))*t_step
print(E2)

## Calculating InnerProduct  ∫0T sl(t)s∗ k(t)dt
signal_conj_multiply = np.multiply(s_1_t, np.conj(s_2_t))
innerProduct = sum(signal_conj_multiply)*t_step   ## = 2.0127308552774957e-16  very close to 0

print(innerProduct)
## wave plot

plt.plot(time, s_1_t)
plt.plot(time, s_2_t)
plt.plot(time, signal_conj_multiply)

plt.xlabel("time")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
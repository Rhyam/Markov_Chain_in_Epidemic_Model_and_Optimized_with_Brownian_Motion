import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

N = 10000
I = [1]
S = [9999]
R = [0]
T = [i for i in range(101)]
r = 10
beta = 0.05
gama = 0.1
for i in range(100):
    S.append(S[i]-r*beta*S[i]*I[i]/N)
    I.append(I[i]+r*beta*S[i]*I[i]/N-gama*I[i])
    R.append(R[i]+gama*I[i])

I = np.array(I)
S = np.array(S)
R = np.array(R)
font1 = {'family' : 'Times New Roman',  'weight' : 'normal',  'size': 15}
font2 = {'family' : 'Times New Roman',  'weight' : 'normal',  'size': 20} 
plt.figure(figsize=(10,6.18), dpi=80)
ax = plt.subplot(1,1,1)

ax.yaxis.set_major_locator(MultipleLocator(1000))
plt.ylim(0, 10000)
plt.xlim(0, 100)

plt.plot(T, S, color='blue', label='Susceptible', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.plot(T, I, color='red', label='Infectious', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.plot(T, R, color='green', label='Recovered', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.ylim(0, 10000)
plt.xlim(0, 100)

plt.title("SIR Model", font=font2)
plt.xlabel("T/day", font=font1)
plt.ylabel("Population", font=font1)
plt.grid()
plt.show()
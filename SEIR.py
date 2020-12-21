import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

N = 10000
I = [1]
E = [0]
S = [9999]
R = [0]
T = [i for i in range(161)]
r = 20
beta = 0.03
gama = 0.1
sigma = 0.1
for i in range(160):
    S.append(S[i]-r*beta*S[i]*I[i]/N)
    E.append(E[i]+r*beta*S[i]*I[i]/N-sigma*E[i])
    I.append(I[i]+sigma*E[i]-gama*I[i])
    R.append(R[i]+gama*I[i])

I = np.array(I)
S = np.array(S)
E = np.array(E)
R = np.array(R)
font1 = {'family' : 'Times New Roman',  'weight' : 'normal',  'size': 15}
font2 = {'family' : 'Times New Roman',  'weight' : 'normal',  'size': 20} 
plt.figure(figsize=(10,6.18), dpi=80)
ax = plt.subplot(1,1,1)

ax.yaxis.set_major_locator(MultipleLocator(1000))
plt.ylim(0, 10000)
plt.xlim(0, 160)

plt.plot(T, S, color='blue', label='Susceptible', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.plot(T, E, color='orange', label='Exposed', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.plot(T, I, color='red', label='Infectious', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.plot(T, R, color='green', label='Recovered', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.title("SEIR Model", font=font2)
plt.xlabel("T/day", font=font1)
plt.ylabel("Population", font=font1)
plt.grid()
plt.show()
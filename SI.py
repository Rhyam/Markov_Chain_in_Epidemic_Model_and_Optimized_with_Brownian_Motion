import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

N = 10000
I = [1]
S = [9999]
T = [i for i in range(201)]
r = 10
beta = 0.01
for i in range(200):
    I.append((1+beta*r)*I[i]-beta*r*I[i]*I[i]/N)
    S.append((1-beta*r)*S[i]+beta*r*S[i]*S[i]/N)

I = np.array(I)
S = np.array(S)
font1 = {'family' : 'Times New Roman',  'weight' : 'normal',  'size': 15}
font2 = {'family' : 'Times New Roman',  'weight' : 'normal',  'size': 20} 
plt.figure(figsize=(10,6.18), dpi=80)
ax = plt.subplot(1,1,1)

ax.yaxis.set_major_locator(MultipleLocator(1000))

plt.plot(T, S, color='blue', label='Susceptible', linewidth=1)
plt.ylim(0, 10000)
hl = plt.legend(loc='upper right', prop=font1, frameon=False)

plt.plot(T, I, color='red', label='Infectious', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)
plt.xlim(0, 200)

plt.title("SI Model", font=font2)
plt.xlabel("T/day", font=font1)
plt.ylabel("Population", font=font1)
plt.grid()
plt.show()
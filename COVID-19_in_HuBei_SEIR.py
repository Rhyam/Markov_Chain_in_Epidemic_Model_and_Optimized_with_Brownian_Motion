import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

T = [i for i in range(77)]
S = []
I = []
R = []
E = []

f = open("s.txt")
lines = f.readlines()
for i in lines:
    S.append(int(i.strip()))

f = open("i.txt")
lines = f.readlines()
for i in lines:
    I.append(int(i.strip()))

f = open("r.txt")
lines = f.readlines()
for i in lines:
    R.append(int(i.strip()))

f = open("e.txt")
lines = f.readlines()
for i in lines:
    E.append(int(i.strip()))

I = np.array(I)
S = np.array(S)
E = np.array(E)
R = np.array(R)
font1 = {'family' : 'Times New Roman',  'weight' : 'normal',  'size': 15}
font2 = {'family' : 'Times New Roman',  'weight' : 'normal',  'size': 20} 
plt.figure(figsize=(10,6.18), dpi=80)
ax = plt.subplot(1,1,1)

ax.yaxis.set_major_locator(MultipleLocator(5000))
plt.ylim(0, 70000)
plt.xlim(0, 80)

plt.plot(T, S, color='blue', label='Susceptible', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.plot(T, E, color='orange', label='Exposed', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.plot(T, I, color='red', label='Infectious', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.plot(T, R, color='green', label='Recovered', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.title("COVID-19 in HuBei by SEIR", font=font2)
plt.xlabel("T/day", font=font1)
plt.ylabel("Population", font=font1)
plt.grid()
plt.show()
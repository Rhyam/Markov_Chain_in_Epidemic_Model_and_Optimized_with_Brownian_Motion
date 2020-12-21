import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

c = 2
deltaI = 0.13
deltaq = 0.13
gamaI = 0.007
gamaH = 0.014
beta = 0.00000000205
q = 0.000001
alpha = 0.00027
I = [786]
E = [4007]
S = [59170000]
R = [31]
Sq = [2776]
Eq = [400]
H = [1186]
T = [i for i in range(71)]
for i in range(70):
    S.append(S[i]+Sq[i]/14-(c*beta+c*q*(1-beta))*S[i]*(I[i]+E[i]))
    E.append(E[i]+c*beta*(1-q)*S[i]*(I[i]+E[i])-E[i]/7)
    I.append(I[i]+E[i]/7-(deltaI+alpha+gamaI)*I[i])
    Sq.append(Sq[i]+c*q*(1-beta)*S[i]*(I[i]+E[i])-Sq[i]/14)
    Eq.append(Eq[i]+c*beta*q*S[i]*(I[i]+E[i])-deltaq*Eq[i])
    H.append(H[i]+deltaI*I[i]+deltaq*Eq[i]-(alpha+gamaH)*H[i])
    R.append(R[i]+gamaI*I[i]+gamaH*H[i])

font1 = {'family' : 'Times New Roman',  'weight' : 'normal',  'size': 15}
font2 = {'family' : 'Times New Roman',  'weight' : 'normal',  'size': 20} 
plt.figure(figsize=(10,6.18), dpi=80)
ax = plt.subplot(1,1,1)

ax.yaxis.set_major_locator(MultipleLocator(10000))
plt.ylim(0, 60000)
plt.xlim(0, 70)

plt.plot(T, E, color='orange', label='Exposed', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.plot(T, I, color='red', label='Infectious', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.title("Improved SEIR Model", font=font2)
plt.xlabel("T/day", font=font1)
plt.ylabel("Population", font=font1)
plt.grid()
plt.show()
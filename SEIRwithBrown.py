import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

x = np.array([2*i+1 for i in range(50)])
y = np.array([2*i+1 for i in range(50)])
x, y = np.meshgrid(x, y)
X = [i for j in x for i in j]
Y = [i for j in y for i in j]
state = [0]*2500
state[random.randint(0,2499)] = 2
"""
originI = []
while(len(originI)<100):
    tmp = random.randint(0,2499)
    if tmp not in originI:
        originI.append(tmp)
for i in originI:
    state[i] = 2
"""
beta = 0.04
multiple = 5
sigma = 2
delta = 1/7
gamma = 0.05
T = [i for i in range(0, 201)]
S = [2499]
E = [0]
I = [1]
R = [0]
#在不考虑恢复率的情况下模拟隔离措施
Quarantined = []
v1 = 1/5
v2 = 1/3

def IinDistance(point, state, X, Y):
    countI2 = 0
    for k in range(2500):
        if X[k]<40 or X[k]>60 or Y[k]<40 or Y[k]>60:
            if (X[k]-X[point])**2+(Y[k]-Y[point])**2 <= 16:
                if state[k]==2:
                    countI2 += 1
    return countI2

def EIinDistance(point, state, X, Y):
    countI2 = 0
    for k in range(2500):
        if X[k]<40 or X[k]>60 or Y[k]<40 or Y[k]>60:
            if (X[k]-X[point])**2+(Y[k]-Y[point])**2 <= 16:
                if state[k]==2 or state[k]==1:
                    countI2 += 1
    return countI2

def EInotinQ(point, state, X, Y):
    countI2 = 0
    for k in range(2500):
        if k not in Quarantined:
            if X[k]<40 or X[k]>60 or Y[k]<40 or Y[k]>60:
                if (X[k]-X[point])**2+(Y[k]-Y[point])**2 <= 16:
                    if state[k]==2 or state[k]==1:
                        countI2 += 1
    return countI2

def EnoInfect():    #潜伏者无传染性
    for j in range(200):
        countS1 = 0
        countI1 = 0
        toE = 0
        number1 = []
        number2 = []
        number3 = []

        for i in range(2500):
            if state[i] == 1:
                number2.append(i)
            if state[i] == 2:
                number3.append(i)
        
            if X[i]>=40 and X[i]<=60 and Y[i]>=40 and Y[i]<=60:
                if state[i] == 0:
                    countS1 += 1
                    number1.append(i)
                if state[i] == 2:
                    countI1 += 1
            else:
                if state[i] == 0:
                    countI2 = IinDistance(i, state, X, Y)
                    tmp = random.random()
                    if tmp < 0.5+countI2*beta/2 and tmp >= 0.5-countI2*beta/2:
                        toE += 1
                        state[i] = 1
        
            
        if round(countS1*countI1*beta*multiple) <= countS1:
            toE1 = np.random.choice(number1, round(countS1*countI1*beta*multiple), replace=False)
        else:
            toE1 = number1
        for i in toE1:
            state[i] = 1
        toE += len(toE1)
        S.append(S[-1]-toE)
        toI1 = np.random.choice(number2, int(E[-1]*delta), replace=False)
        for i in toI1:
            state[i] = 2
        E.append(E[-1]+toE-len(toI1))
        toR1 = np.random.choice(number3, int(I[-1]*gamma), replace=False)
        for i in toR1:
            state[i] = 3
        I.append(I[-1]+len(toI1)-len(toR1))
        R.append(R[-1]+len(toR1))

        for i in range(2500):
            x_tmp = X[i] + sigma * np.random.randn()
            if x_tmp > 100:
                X[i] = 200 - x_tmp
            elif x_tmp < 0:
                X[i] = 0 - x_tmp
            else:
                X[i] = x_tmp

            y_tmp = Y[i] + sigma * np.random.randn()
            if y_tmp > 100:
                Y[i] = 200 - y_tmp
            elif y_tmp < 0:
                Y[i] = 0 - y_tmp
            else:
                Y[i] = y_tmp
        print(S[-1],E[-1],I[-1],R[-1])

def EwithInfect():    #潜伏者具有和感染者相同的传染性
    for j in range(200):
        countS1 = 0
        countI1 = 0
        toE = 0
        number1 = []
        number2 = []
        number3 = []

        for i in range(2500):
            if state[i] == 1:
                number2.append(i)
            if state[i] == 2:
                number3.append(i)
        
            if X[i]>=40 and X[i]<=60 and Y[i]>=40 and Y[i]<=60:
                if state[i] == 0:
                    countS1 += 1
                    number1.append(i)
                if state[i] == 2 or state[i] == 1:
                    countI1 += 1
            else:
                if state[i] == 0:
                    countI2 = EIinDistance(i, state, X, Y)
                    tmp = random.random()
                    if tmp < 0.5+countI2*beta/2 and tmp >= 0.5-countI2*beta/2:
                        toE += 1
                        state[i] = 1
        
            
        if round(countS1*countI1*beta*multiple) <= countS1:
            toE1 = np.random.choice(number1, round(countS1*countI1*beta*multiple), replace=False)
        else:
            toE1 = number1
        for i in toE1:
            state[i] = 1
        toE += len(toE1)
        S.append(S[-1]-toE)
        toI1 = np.random.choice(number2, int(E[-1]*delta), replace=False)
        for i in toI1:
            state[i] = 2
        E.append(E[-1]+toE-len(toI1))
        toR1 = np.random.choice(number3, int(I[-1]*gamma), replace=False)
        for i in toR1:
            state[i] = 3
        I.append(I[-1]+len(toI1)-len(toR1))
        R.append(R[-1]+len(toR1))

        for i in range(2500):
            x_tmp = X[i] + sigma * np.random.randn()
            if x_tmp > 100:
                X[i] = 200 - x_tmp
            elif x_tmp < 0:
                X[i] = 0 - x_tmp
            else:
                X[i] = x_tmp

            y_tmp = Y[i] + sigma * np.random.randn()
            if y_tmp > 100:
                Y[i] = 200 - y_tmp
            elif y_tmp < 0:
                Y[i] = 0 - y_tmp
            else:
                Y[i] = y_tmp
        print(S[-1],E[-1],I[-1],R[-1])

def Quarantine():    #潜伏者具有和感染者相同的传染性
    for j in range(50):
        countS1 = 0
        countI1 = 0
        toE = 0
        toI = 0
        number1 = []
        number2 = []
        number3 = []

        for i in range(2500):
            if i not in Quarantined:
                if state[i] == 1:
                    number2.append(i)
                if state[i] == 2:
                    number3.append(i)
            else:
                if state[i] == 1:
                    tmp = random.random()
                    if tmp < 0.5+delta/2 and tmp >= 0.5-delta/2:
                        toI += 1
                        state[i] = 2
        
            if X[i]>=40 and X[i]<=60 and Y[i]>=40 and Y[i]<=60:
                if state[i] == 0:
                    countS1 += 1
                    number1.append(i)
                if state[i] == 2 or state[i] == 1:
                    if i not in Quarantined:
                        countI1 += 1
            else:
                if state[i] == 0:
                    countI2 = EInotinQ(i, state, X, Y)
                    tmp = random.random()
                    if tmp < 0.5+countI2*beta/2 and tmp >= 0.5-countI2*beta/2:
                        toE += 1
                        state[i] = 1
            
        if round(countS1*countI1*beta*multiple) <= countS1:
            toE1 = np.random.choice(number1, round(countS1*countI1*beta*multiple), replace=False)
        else:
            toE1 = number1
        for i in toE1:
            state[i] = 1
        toE += len(toE1)
        S.append(S[-1]-toE)
        if int(E[-1]*(delta+v1))<=len(number2):
            toI1 = np.random.choice(number2, int(E[-1]*(delta+v1)), replace=False)
        else:
            toI1 = number2
        rate = delta/(delta+v1)
        for i in toI1:
            if random.random() < rate:
                state[i] = 2
                toI += 1
            else:
                Quarantined.append(i)
        E.append(E[-1]+toE-toI)
        if int(I[-1]*v2)<=len(number3):
            toR1 = np.random.choice(number3, int(I[-1]*v2), replace=False)
        else:
            toR1 = number3
        for i in toR1:
            Quarantined.append(i)
        I.append(I[-1]+toI)

        for i in range(2500):
            x_tmp = X[i] + sigma * np.random.randn()
            if x_tmp > 100:
                X[i] = 200 - x_tmp
            elif x_tmp < 0:
                X[i] = 0 - x_tmp
            else:
                X[i] = x_tmp

            y_tmp = Y[i] + sigma * np.random.randn()
            if y_tmp > 100:
                Y[i] = 200 - y_tmp
            elif y_tmp < 0:
                Y[i] = 0 - y_tmp
            else:
                Y[i] = y_tmp
        print(S[-1],E[-1],I[-1])
"""二维随机游走散点
plt.plot(X, Y,
         color='#4169E1',  # 全部点设置为红色
         marker='.',  # 点的形状为圆点
         linestyle='')  # 线型为空，也即点与点之间不用线连接
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.title("Brownian Motion State")
plt.show()
"""
#EwithInfect()和EnoInfect()二选一
#Quarantine()隔离措施研究

font1 = {'family' : 'Times New Roman',  'weight' : 'normal',  'size': 15}
font2 = {'family' : 'Times New Roman',  'weight' : 'normal',  'size': 20} 
plt.figure(figsize=(10,6.18), dpi=80)
ax = plt.subplot(1,1,1)

ax.yaxis.set_major_locator(MultipleLocator(500))
plt.ylim(0, 2500)
#plt.xlim(0, 200)
plt.xlim(0, len(T)-1)

plt.plot(T, S, color='blue', label='Susceptible', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.plot(T, E, color='orange', label='Exposed', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)

plt.plot(T, I, color='red', label='Infectious', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)
"""
plt.plot(T, R, color='green', label='Recovered', linewidth=1)
plt.legend(loc='upper right', prop=font1, frameon=False)
"""
plt.title("SEIR with BM & Quarantine", font=font2)
plt.xlabel("T/day", font=font1)
plt.ylabel("Population", font=font1)
plt.grid()
plt.show()
#Monte Carlo Q1:
import random
import math
import matplotlib.pyplot as plt
def decay(n0,alpha,dt):
    n=n0
    x=[]
    y=[]
    t=0
    while n>(n0/1000):
        c=n
        t=t+dt
        for i in range(c):
            p = random.uniform(0,1)
            if p<=(alpha*dt):
                n = n-1
        x.append(t)
        y.append(n)
    plt.plot(x,y)
    plt.xlabel("time")
    plt.ylabel("Number of atoms remaining")
    plt.title("N v t")
    plt.show()
def eplot(n0,alpha):
    n=n0
    t=0
    x=[]
    y=[]
    while n>(n0/1000):
        n = n*(math.e**(-alpha))
        t = t+1
        x.append(t)
        y.append(n)
    plt.plot(x,y)
    plt.xlabel("time")
    plt.ylabel("Number of atoms remaining")
    plt.title("N v t")
    plt.show()
                
    return n
#1
decay(100,0.01,1)
decay(5000,0.03,1)
eplot(100,0.01)
eplot(5000,0.03)


import math
import random
import statistics
import matplotlib.pyplot as plt
#Monte Carlo Q2:
def decayfinito(n0,alpha,dt,t):
    n=n0
    for j in range(int(t/dt)):
        c = n
        for i in range(c):
            p = random.uniform(0,1)
            if p<=(alpha*dt):
                n = n-1
    return n
    
#2a
a=[]
b=[]
for i in range(1000):
    a.append(decayfinito(500, 0.00004, 10, 100))
plt.hist(a)
plt.show()
y = statistics.mean(a)
for i in range(len(a)):
    b = (math.e**(-y)*(y**a[i]))/math.factorial(a[i])
plt.plot(x,y)
plt.xlabel("N after 100s")
plt.ylabel("P(N)")
plt.title("Poissonian distribution for alpha = 0.00004")
plt.show()

#2b
a=[]
for i in range(1000):
    a.append(decayfinito(500, 0.00002, 10, 100))
plt.hist(a)
plt.show()
y = statistics.mean(a)
for i in range(len(a)):
    b = (math.e**(-y)*(y**a[i]))/math.factorial(a[i])
plt.plot(x,y)
plt.xlabel("N after 100s")
plt.ylabel("P(N)")
plt.title("Poissonian distribution for alpha = 0.00002")
plt.show()

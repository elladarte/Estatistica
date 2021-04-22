from numpy.random import exponential, seed
from statistics import mean, variance

theta = 2.0
N = 10000
Ta = 50
T = []
t = 0.0
send(1995, 2)

for i in range(N):
    X = exponential(1.0/theta, Ta)
    t = len(X)/sum(X)
    T.append(t)

vies = mean(T) - theta
EQM = variance(T) + vies**2

print('theta      =     {:.4f}'.format(theta))
print('E(T)       =     {:.4f}'.format(mean(T)))
print('vies       =     {:.4f}'.format(vies))
print('EQM        =     {:.4f}'.format(EQM))

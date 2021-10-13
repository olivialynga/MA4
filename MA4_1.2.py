import math
import random
import functools

n=input('slumpvisa koordinater: ')
d=input('dimensioner: ')

lst=[[random.uniform(-1.0000, 1.0000) for i in range(int(d))] for i in range(0, int(n))]
n_in=0
for koord in lst:
    V1=list(map(lambda x: x**2, koord))
    V2=sum(V1)
    if V2<=1:
        n_in+=1
        
#V_approx=2**int(d)*(int(n)/n_in)
V_approx=2**int(d)*(n_in/int(n))
print(f'Approximerade värdet: {V_approx}')
r=1
V=((float(math.pi))**(int(d)/2))/(math.gamma((int(d)/2)+1))*r**int(d)
print(f'Värdet: {V}')



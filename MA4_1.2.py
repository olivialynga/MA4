import math
import random
import functools
import time 


n=input('slumpvisa koordinater: ')
d=input('dimensioner: ')

tstart = time . perf_counter ()
lst=[[random.uniform(-1.0000, 1.0000) for i in range(int(d))] for i in range(0, int(n))]
n_in=0

for koord in lst:
    V1=list(map(lambda x: x**2, koord))
    V2=sum(V1)
    if V2<=1:
        n_in+=1
        
tstop = time . perf_counter ()

V_approx=2**int(d)*(n_in/int(n))
print(f'Approximerade värdet: {V_approx}')
r=1
V=((float(math.pi))**(int(d)/2))/(math.gamma((int(d)/2)+1))*r**int(d)
print(f'Värdet: {V}')
print ( f"Measured time : {tstop - tstart } seconds ")




from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
import random

def hyper_s(n, d):
    lst=[[random.uniform(-1.0000, 1.0000) for i in range(int(d))] for i in range(0, int(n))]
    n_in=0
    for koord in lst:
        V1=list(map(lambda x: x**2, koord))
        V2=sum(V1)
        if V2<=1:
            n_in+=1
    V_approx=2**int(d)*(n_in/int(n))
    return V_approx

if __name__=='__main__':
    start = pc()
    n_lst=[100000 for x in range(10)]
    d_lst=[11 for x in range(10)]
    with future.ProcessPoolExecutor() as ex:
        results=list(ex.map(hyper_s, n_lst, d_lst))
        results=(lambda x,y: x+y/float(len(results)), results)

    end=pc()
    print(f'Process took {round(end-start, 2)} seconds')

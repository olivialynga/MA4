import math
import random
import matplotlib.pyplot as plt

n= [1000]
def func_pi(n):
    nc=0
    plt.figure(figsize=[5,5])
    for i in range(0, (n)):
        x = (random.uniform(-1.0000, 1.0000))
        y = (random.uniform(-1.0000, 1.0000))
        if (x**2+y**2)<=1.0:
            nc+=1
            plt.plot(x,y,'ro')
        else:
            plt.plot(x,y,'bo')


    approx_pi = 4*(nc/int(n))
    print(f'pi: {math.pi}\napproximation: {approx_pi} med {n} slumpvariabler\n{nc} punkter i cirkeln')


    plt.show()

func_pi(1000)
func_pi(10000)
func_pi(100000)


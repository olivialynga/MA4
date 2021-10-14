import time
import matplotlib
import matplotlib.pyplot as plt

def fib_py(n):
    if n<=1:
        return n
    else:
        return (fib_py(n-1) + fib_py(n-2))

length = [x for x in range(35)]

fib_py_time = []

for i in length:
    ts = time.time()
    fib_py(i)
    fib_py_time.append(time.time()-ts)

plt.plot(length, fib_py_time)
plt.show()
    

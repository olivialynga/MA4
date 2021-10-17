#!/usr/bin/env python3

from integer import Integer
import matplotlib
import matplotlib.pyplot as plt
import time

def fib_py(n):
    if n<=1:
        return n
    else:
        return (fib_py(n-1) + fib_py(n-2))

length = [x for x in range(35)]

fib_py_time = []

for i in length:
    ts= time.time()
    fib_py(i)
    fib_py_time.append(time.time()-ts)

plt.plot(length, fib_py_time)
plt.show()

def main():
    f = Integer(5)
    print(f.get())
    f.set(7)
    print(f.get())

    fib_c_time = []
    length_c = [x for x in range(35)]
    for n in length_c:
        t_s=time.time()
        f=Integer(n)
        f.fib()
        fib_c_time.append(time.time()-t_s)
    plt.plot(length_c, fib_c_time)
    plt.xlabel('n')
    plt.ylabel('sekunder')
    plt.title('tid fib')
    matplotlib.pyplot.savefig("time.perf_counter.png")
    plt.show()


if __name__ == '__main__':
	main()

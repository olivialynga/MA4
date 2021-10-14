#!/usr/bin/env python3

from integer import Integer
import matplotlib
import matplotlib.pyplot as plt

def fib_py(n):
    if n<=1:
        return n
    else:
        return (fib_py(n-1) + fib_py(n-2))

length = [x for x in range(25)]

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
	f=Integer(n)

	f.fib()

if __name__ == '__main__':
	main()

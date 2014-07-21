from timeit import Timer
import sys, os

def fib(x):
    return 1 if x < 2 else fib(x-1) + fib(x-2)

if __name__ == "__main__":
    t = Timer("fib(30)", "from __main__ import fib")
    print(t.timeit(1))
    print(sys.version)
    os.system("pause")



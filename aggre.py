import numpy as np
import timeit

x = np.arange(1, 6)
print(x)
print("add reduce: ",np.add.reduce(x))
print("mul reduce: ",np.multiply.reduce(x))
print("add accumulate: ", np.add.accumulate(x))
print("mul accumulate: ", np.multiply.accumulate(x))

x = np.arange(1, 6)
print(np.multiply.outer(x, x))

L = np.random.random(100)
print(np.sum(L))

big_array = np.random.rand(1000000)
start_time = timeit.default_timer()
print(sum(big_array))
print(timeit.default_timer() - start_time, "\n")

start_time = timeit.default_timer()
print(np.sum(big_array))
print(timeit.default_timer() - start_time, "\n")



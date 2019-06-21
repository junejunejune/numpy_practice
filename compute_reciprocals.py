import numpy as np
from timeit import default_timer as timer

np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0/values[i]
    return output

values = np.random.randint(1, 100, size=1000000)

start = timer()
result = compute_reciprocals(values)
end = timer()

print(result)
print(end-start)

start = timer()
result = (1.0/values)
end = timer()

print()
print(result)
print(end-start)

result = np.arange(5) / np.arange(1, 6)
print("\n%s" %result)

result = np.arange(9).reshape(3,3)
print("\n%s"%result)
print(2**result)

x = np.arange(4)
print("\nx =", x)
print("x + 5 =", x+5)
print("x - 5 =", x-5)
print("x * 2 =", x*2)
print("x / 2 =", x/2)
print("x // 2 =", x//2)

print("-x =", -x)
print("x**2 =", x**2)
print("x%2 =", x%2)

print("\ncombi =", -(0.5*x+1)**2)

print(np.add(x,2))

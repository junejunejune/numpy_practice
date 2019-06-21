import numpy as np


print()
M = np.ones((3,2))
a = np.arange(3)
print("M: ", M)
print("a: ", a)

print()
print("a: ", a)
print("0: ",a[:, np.newaxis])
print("2: ",M+a[:, np.newaxis])

X = np.random.random((10, 3))
print("\n", X)
Xmean = X.mean(0)
print(Xmean)
X_centered = X-Xmean
print(X_centered.mean(0))

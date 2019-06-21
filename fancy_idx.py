import numpy as np

X = np.arange(12).reshape((3,4))

row = np.array([0,1,2])
col = np.array([2,1,3])
print("row: ", row)
print("col: ", col)
print(X)
print("X: ", X[row, col])

print("\nnewaxis:\n", row[:, np.newaxis])

x= np.zeros(10)
i = [2,3,3,4,4,4]
np.add.at(x, i, 1)
print(x)

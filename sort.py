import numpy as np

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x

x = np.array([2,1,4,3,5])
print(selection_sort(x))

x = np.array([2,1,4,3,5])
print(bogosort(x))

x = np.array([2,1,4,3,5])
print(np.sort(x))

x = np.array([7,2,3,1,6,5,4])
print(np.partition(x,3))






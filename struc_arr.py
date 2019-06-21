import numpy as np

name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})

data['name'] = name
data['age'] = age
data['weight'] = weight

print(data)
print(data['name'])
print(data[0])
print(data[-1]['name'])


tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3,3))])
X = np.zeros(1, dtype=tp)
print(X[0])
print(X['mat'][0]) 

import numpy as np
from scipy import special

x =[1, 5, 10]
print("gamma(x) =", special.gamma(x))
print("ln|gamma(x)=", special.gammaln(x))
print("beta(x, 2)", special.beta(x, 2))

x = np.array([0,0.3,0.7,1.0])
print("\nerf(x) =", special.erf(x))
print("erfc(x) =", special.erfc(x))
print("erfinv(x) =", special.erfinv(x))

x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)

y = np.zeros(10)
np.power(2, x , out=y[::2])
print(y)



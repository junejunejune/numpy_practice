import numpy as np

theta = np.linspace(0, np.pi, 3)

print("theta =", theta)
print("sin(theta)=", np.sin(theta))
print("cos(theta)=", np.cos(theta))
print("tan(theta)=", np.tan(theta))

x=[-1, 0, 1]
print("x =", x)
print("arcsin(x) =", np.arcsin(x))
print("arccos(x) =", np.arccos(x))
print("arctan(x) =", np.arctan(x))

x=[1, 2, 3]
print("\nx =", x)
print("e^x =", np.exp(x))
print("2^x =", np.exp2(x))
print("3^x =", np.power(3, x))

x=[1,2,4,10]
print("\nx =", x)
print("ln(x) =", np.log(x))
print("log2(x) =", np.log2(x))
print("log10(x) =", np.log10(x))

x = [0, 0.001, 0.01, 0.1]
print("\nexp(x) -1 =", np.expm1(x))
print("log(1 + x) =", np.log1p(x))



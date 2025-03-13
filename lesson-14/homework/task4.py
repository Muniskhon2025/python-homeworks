import numpy as np

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def custom_power(base, exponent):
    return base ** exponent

# Vectorizing the functions
vectorized_f_to_c = np.vectorize(fahrenheit_to_celsius)
vectorized_power = np.vectorize(custom_power)

# Arrays
temperatures_f = np.array([32, 68, 100, 212, 77])
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])

# Convert to Celsius
temperatures_c = vectorized_f_to_c(temperatures_f)

# Calculate power
powers = vectorized_power(bases, exponents)

# Solve system of equations
A = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
B = np.array([7, 4, 5])
solutions = np.linalg.solve(A, B)

# Solve electrical circuit equations
A_circuit = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
B_circuit = np.array([12, -5, 15])
currents = np.linalg.solve(A_circuit, B_circuit)

print(temperatures_c)
print(powers)
print(solutions)
print(currents)

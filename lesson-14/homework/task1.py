import numpy as np

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

# Vectorizing the function
vectorized_f_to_c = np.vectorize(fahrenheit_to_celsius)

# Array of Fahrenheit temperatures
temperatures_f = np.array([32, 68, 100, 212, 77])

# Convert to Celsius
temperatures_c = vectorized_f_to_c(temperatures_f)

print(temperatures_c)

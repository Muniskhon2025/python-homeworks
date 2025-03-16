import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Basic Plotting
x = np.linspace(-10, 10, 100)
y = x**2 - 4*x + 4
plt.figure()
plt.plot(x, y, label=r"$f(x) = x^2 - 4x + 4$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Quadratic Function Plot")
plt.legend()
plt.grid()
plt.show()

# 2. Sine and Cosine Plot
x = np.linspace(0, 2*np.pi, 100)
plt.figure()
plt.plot(x, np.sin(x), linestyle='-', marker='o', color='b', label=r"$\sin(x)$")
plt.plot(x, np.cos(x), linestyle='--', marker='s', color='r', label=r"$\cos(x)$")
plt.xlabel("x")
plt.ylabel("Value")
plt.title("Sine and Cosine Plot")
plt.legend()
plt.grid()
plt.show()

# 3. Subplots
x = np.linspace(-2, 2, 100)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Top-left: x^3
axs[0, 0].plot(x, x**3, color='g')
axs[0, 0].set_title("f(x) = x^3")
axs[0, 0].set_xlabel("x")
axs[0, 0].set_ylabel("f(x)")

# Top-right: sin(x)
axs[0, 1].plot(x, np.sin(x), color='r')
axs[0, 1].set_title("f(x) = sin(x)")
axs[0, 1].set_xlabel("x")
axs[0, 1].set_ylabel("f(x)")

# Bottom-left: e^x
axs[1, 0].plot(x, np.exp(x), color='b')
axs[1, 0].set_title("f(x) = e^x")
axs[1, 0].set_xlabel("x")
axs[1, 0].set_ylabel("f(x)")

# Bottom-right: log(x+1)
x_pos = np.linspace(0, 2, 100)
axs[1, 1].plot(x_pos, np.log(x_pos+1), color='purple')
axs[1, 1].set_title("f(x) = log(x+1)")
axs[1, 1].set_xlabel("x")
axs[1, 1].set_ylabel("f(x)")

plt.tight_layout()
plt.show()

# 4. Scatter Plot
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
plt.figure()
plt.scatter(x, y, c=np.random.rand(100), marker='o', cmap='viridis', edgecolors='black')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Random Scatter Plot")
plt.grid()
plt.show()

# 5. Histogram
data = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(data, bins=30, alpha=0.7, color='b', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normally Distributed Data")
plt.grid()
plt.show()

# 6. 3D Plotting
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
plt.colorbar(surf)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("f(x, y)")
ax.set_title("3D Surface Plot")
plt.show()

# 7. Bar Chart
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.figure()
plt.bar(products, sales, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales Data")
plt.show()

# 8. Stacked Bar Chart
categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']
data = np.random.randint(10, 50, (3, 4))

plt.figure()
bottom_values = np.zeros(4)
for i in range(3):
    plt.bar(time_periods, data[i], bottom=bottom_values, label=categories[i])
    bottom_values += data[i]

plt.xlabel("Time Periods")
plt.ylabel("Value")
plt.title("Stacked Bar Chart")
plt.legend()
plt.show()

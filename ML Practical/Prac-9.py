import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2)

# Plot the sine function on the first subplot and color it red
ax1.plot(x, y_sin, color='red')

# Label the axes and title the first subplot
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Sine Function')

# Plot the cosine function on the second subplot and color it blue
ax2.plot(x, y_cos, color='blue')

# Label the axes and title the second subplot
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Cosine Function')

# Display the plot
plt.show()

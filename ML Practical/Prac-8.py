import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
data = np.random.normal(size=1000)

# Create a histogram
plt.hist(data, bins=30)

# Label the axes and title the plot
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')

# Display the plot
plt.show()

# Generate some data
x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the sine and cosine functions
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')

# Label the axes and title the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')

# Add a legend
plt.legend()

# Display the plot
plt.show()

# Generate some random data
x = np.random.normal(size=100)
y = np.random.normal(size=100)

# Create a scatter plot
plt.scatter(x, y)

# Label the axes and title the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot of Random Data')

# Display the plot
plt.show()

# Generate some data
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 24, 16, 30, 18]

# Create a bar chart
plt.bar(x, y)

# Label the axes and title the plot
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')

# Display the plot
plt.show()
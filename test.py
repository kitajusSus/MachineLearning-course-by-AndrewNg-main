import matplotlib.pyplot as plt
# Create some data
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# Plot the data
plt.plot(x_values, y_values)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Matplotlib Plot')

# Display the plot
plt.show()
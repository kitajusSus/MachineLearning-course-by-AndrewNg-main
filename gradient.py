
import numpy as np
import matplotlib.pyplot as plt

# Training data
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([10, 20, 30])

# Initialization of weights and bias
w = np.zeros(x.shape[1])
b = 0


alpha = 0.01

num_iterations = 1000

# Lists to store weights and bias values for each iteration
w_history = [w.copy()]
b_history = [b]

# Gradient descent implementation with visualization
for i in range(num_iterations):
    y_pred = np.dot(x, w) + b

    # Calculate gradients (optimized for clarity)
    dw = (1 / len(x)) * np.dot(x.T, (y_pred - y))
    db = (1 / len(x)) * np.sum(y_pred - y)

    # Update weights and bias
    w = w - alpha * dw
    b = b - alpha * db

    # Store weights and bias values for plotting
    w_history.append(w.copy())
    b_history.append(b)

# Print final results
print("Final Wages:", w)
print("Final Bias:", b)

# Create separate plots for weights and bias
plt.figure(figsize=(10, 6))

# Plot weights
for i in range(len(w_history[0])):
    plt.plot(range(num_iterations + 1), [w[i] for w in w_history], label=f'Weight W{i+1}')

# Plot bias
plt.plot(range(num_iterations + 1), b_history, label='Bias')

plt.xlabel('Iteration')
plt.ylabel('Value')
plt.title('Weight and Bias Changes during Gradient Descent')
plt.legend()
plt.grid(True)
plt.show()
    



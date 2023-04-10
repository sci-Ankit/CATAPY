import numpy as np

# Define the transformation matrix
T = np.array([[1, 0], [1, 0]])

# Define the vector
v = np.array([1, 0])

# Multiply the vector with the transformation matrix
result = T.dot(v)

print(result)
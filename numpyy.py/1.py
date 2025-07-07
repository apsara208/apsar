import numpy as np
#1. conversion from other data structures:
print(np.__version__)
# Create a 1D NumPy array
arr = np.array([10, 20, 30, 40, 50])
print("Original array:", arr)

# Multiply all elements by 2
doubled = arr * 2
print("Doubled array:", doubled)

# Calculate the mean and standard deviation
mean = np.mean(arr)
std_dev = np.std(arr)

print("Mean:", mean)
print("Standard Deviation:", std_dev)




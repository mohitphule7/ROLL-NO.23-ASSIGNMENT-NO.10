mport numpy as np

# Create a 1D array containing numbers 1 to 10
arr = np.arange(1, 11)

# Display the array
print("Original Array:")
print(arr)

# Display number of dimensions
print("\nNumber of dimensions:")
print(arr.ndim)

# Display shape of the array
print("\nShape of the array:")
print(arr.shape)

# Display size of the array
print("\nNumber of elements:")
print(arr.size)

# Display data type
print("\nData type of array:")
print(arr.dtype)

# Display first element
print("\nFirst element:")
print(arr[0])

# Display last element
print("\nLast element:")
print(arr[-1])

# Display first five elements
print("\nFirst five elements:")
print(arr[:5])

# Display last five elements
print("\nLast five elements:")
print(arr[5:])

# Calculate sum
print("\nSum of elements:")
print(np.sum(arr))

# Calculate average
print("\nAverage of elements:")
print(np.mean(arr))

# Calculate maximum
print("\nMaximum element:")
print(np.max(arr))

# Calculate minimum
print("\nMinimum element:")
print(np.min(arr))

# Display elements greater than 5
print("\nElements greater than 5:")
print(arr[arr > 5])
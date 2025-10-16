import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)

arr3 = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])
print(arr3)
print("\n")

#Numpy Function

print("Original array:")
print(arr)
print()

# 1. Sum of all elements
print("1. Sum:", np.sum(arr))

# 2. Mean of elements
print("2. Mean:", np.mean(arr))

# 3. Median of elements
print("3. Median:", np.median(arr))

# 4. Standard deviation
print("4. Standard Deviation:", np.std(arr))

# 5. Variance
print("5. Variance:", np.var(arr))

# 6. Minimum element
print("6. Minimum:", np.min(arr))

# 7. Maximum element
print("7. Maximum:", np.max(arr))

#8 Reshape Array
new_arr = arr.reshape(1, 5)  # 1 row, 5 columns
print(new_arr)

# 9. Square root of each element
print("9. Square Root:", np.sqrt(arr))

# 10. Element-wise exponential (e^x)
print("10. Exponential:", np.exp(arr))

"""
  An array is a data structure that can store a collection of elements, usually of the same data type, in a contiguous block of memory. Arrays allow you to store and access elements efficiently using an index.
  The array module in Python does not support mixed data types; it only supports arrays with elements of the same data type.
  In NumPy arrays, when you create an array with elements of different data types, NumPy will convert all elements to the same type to ensure homogeneity.
  Use lists or NumPy arrays for strings.
"""

# Importing the 'array' module as 'arr' for creating a standard array
import array as arr

# Importing the 'numpy' library as 'np' for creating a NumPy array
import numpy as np

# Creating an array of integers using the 'array' module
my_array1 = arr.array('i', [1, 2, 3])

# Creating a NumPy array of strings
my_array2 = np.array(['a', 'b', 'c'])

# Creating a NumPy array of integers
my_array3 = np.array([1, 2, 3])

# Creating a NumPy array of mixed data type. Notice how it converts into same data type.
my_array4 = np.array(['a', 'b', 'c', 1, 2, 3])

# Printing the standard array and its type
print(my_array1)         # Output: array('i', [1, 2, 3])
print(type(my_array1))   # Output: <class 'array.array'>

# Printing the NumPy array and its type
print(my_array2)         # Output: ['a' 'b' 'c']
print(type(my_array2))   # Output: <class 'numpy.ndarray'>

# Printing the NumPy array and its type
print(my_array3)         # Output: [1 2 3]
print(type(my_array3))   # Output: <class 'numpy.ndarray'>

# Printing the NumPy array and its type
print(my_array4)         # Output: ['a' 'b' 'c' '1' '2' '3']
print(type(my_array4))   # Output: <class 'numpy.ndarray'>
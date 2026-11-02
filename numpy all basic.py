"""
NUMPY COMPLETE BEGINNER CHEAT SHEET
===================================
One-file reference for learning the core NumPy syntax.

Install:
    python -m pip install numpy

Run:
    python numpy_complete_guide.py

In VS Code:
    1. Save this file as numpy_complete_guide.py
    2. Select the Python interpreter where NumPy is installed.
    3. Run the file.

Note:
    This file is a learning reference. It prints examples from each section.
    You can uncomment or edit examples to practise.
"""

import numpy as np


def section(title):
    print("\n" + "=" * 75)
    print(title)
    print("=" * 75)


# 1. IMPORT AND VERSION
section("1. IMPORT, VERSION, AND HELP")
print("NumPy version:", np.__version__)
# help(np.array)


# 2. CREATING ARRAYS
section("2. CREATING ARRAYS")
a = np.array([10, 20, 30, 40])
b = np.array([[1, 2, 3], [4, 5, 6]])
print("1D array:", a)
print("2D array:\n", b)
print("Tuple input:", np.array((1, 2, 3)))
print("Nested list:", np.array([[1, 2], [3, 4]]))
print("Zeros:", np.zeros(5))
print("Zeros 2D:\n", np.zeros((2, 3)))
print("Ones:\n", np.ones((2, 3)))
print("Constant:", np.full((2, 3), 7))
print("Identity matrix:\n", np.eye(3))
print("Diagonal matrix:\n", np.diag([2, 4, 6]))
print("Empty array (values are uninitialized):", np.empty(3))
print("Range:", np.arange(0, 10, 2))
print("Evenly spaced:", np.linspace(0, 1, 5))
print("Log spaced:", np.logspace(1, 3, 3))
print("Uninitialized integer array:", np.empty((2, 2), dtype=int))


# 3. ARRAY PROPERTIES
section("3. ARRAY PROPERTIES")
x = np.array([[10, 20, 30], [40, 50, 60]])
print("Array:\n", x)
print("Dimensions:", x.ndim)
print("Shape:", x.shape)
print("Total elements:", x.size)
print("Data type:", x.dtype)
print("Bytes per element:", x.itemsize)
print("Total bytes:", x.nbytes)
print("Transpose:\n", x.T)


# 4. DATA TYPES AND CONVERSION
section("4. DATA TYPES AND CONVERSION")
integers = np.array([1, 2, 3], dtype=np.int32)
decimals = np.array([1, 2, 3], dtype=float)
print("Integer dtype:", integers.dtype)
print("Float dtype:", decimals.dtype)
print("Convert to float:", integers.astype(float))
print("Convert to integer:", decimals.astype(int))
print("Common dtypes: int8, int16, int32, int64, float16, float32, float64, bool, str")
print("Boolean array:", np.array([True, False, True], dtype=bool))


# 5. INDEXING
section("5. INDEXING")
arr = np.array([10, 20, 30, 40, 50])
matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("First:", arr[0])
print("Last:", arr[-1])
print("2D row 0, column 1:", matrix[0, 1])
print("First row:", matrix[0])
print("Second column:", matrix[:, 1])
print("Last row, last column:", matrix[-1, -1])


# 6. SLICING
section("6. SLICING")
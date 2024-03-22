# Advanced Matrix Operations

This project provides a Python implementation of advanced matrix operations, extending basic functionality with features like matrix hashing and customized equality checks. It utilizes the NumPy library for efficient matrix computations.

## Installation

To install the required packages, please run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use the matrix functionalities, you can import the `AdvancedMatrix` class from the `matrix.py` file and then create instances of `AdvancedMatrix`:

```python
from matrix import AdvancedMatrix
import numpy as np

# Create two matrices
A = AdvancedMatrix(np.array([[1, 2], [3, 4]]))
B = AdvancedMatrix(np.array([[5, 6], [7, 8]]))

# Perform matrix multiplication
C = A @ B
```

You can also check the equality and compute the hash of a matrix:

```python
print(A == B)  # Checks if matrices A and B are equal
print(hash(A))  # Returns the hash of matrix A
```

## Files

- `AdvancedMatrix.py`: Main script demonstrating the advanced matrix operations.
- `matrix_mixins.py`: Contains the mixin classes used for extending matrix functionalities.
- `matrix.py`: Defines the `AdvancedMatrix` class and its methods.

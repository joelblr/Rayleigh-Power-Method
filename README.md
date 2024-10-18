# Rayleigh Quotient Iteration and Power Method

This repository contains Python implementations of the **Rayleigh Quotient Iteration** and **Power Method** for finding the dominant eigenvalue and eigenvector of a matrix.

## Table of Contents
- [Overview](#overview)
- [Methods Implemented](#methods-implemented)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview

The **Rayleigh Quotient Iteration** and **Power Method** are iterative algorithms used to compute the dominant eigenvalue and the corresponding eigenvector of a square matrix. These methods are particularly useful in numerical linear algebra, especially for large sparse matrices.

- **Rayleigh Quotient Iteration**: An iterative method for approximating both the eigenvalue and eigenvector of a matrix. It is a refined technique that converges faster than the Power Method, particularly for matrices with distinct eigenvalues.
- **Power Method**: A simpler iterative method to compute the dominant eigenvalue (the one with the largest magnitude) and its corresponding eigenvector.

## Methods Implemented

- **Rayleigh Quotient Iteration**: An iterative process used to approximate an eigenvalue and eigenvector pair.
- **Power Method**: Computes the dominant eigenvalue and eigenvector using an iterative approach based on repeated matrix-vector multiplications.

## Getting Started

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/joelblr/Rayleigh-Power-Method.git
cd Rayleigh-Power-Method
```

## Requirements
This project requires Python 3.x along with the following libraries:

`numpy`: For handling matrix and vector operations.

## Install the dependencies using pip:

```bash
pip install numpy
```

## Usage
Each method is implemented in a separate Python script. You can run the Rayleigh Quotient Iteration or Power Method by executing the respective script.

To run the Script :
```bash
python run.py
```

## Example
Both scripts take as input a matrix for which the dominant eigenvalue and eigenvector need to be computed. You can modify the matrix inside the Python scripts or pass it as an input, depending on how you choose to implement the input system.

```python
matrix = np.array([[4, 1], [2, 3]])
```

## Contributing
If you'd like to contribute to this repository, feel free to fork it, make your changes, and submit a pull request. Contributions to improve the code, add features, or fix bugs are always welcome!
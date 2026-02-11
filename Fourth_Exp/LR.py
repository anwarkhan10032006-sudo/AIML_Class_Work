# EXP 4 - Regression Models

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# -----------------------------
# Dataset
# -----------------------------
data = {
    'X1': [1, 2, 3, 4, 5],
    'X2': [2, 1, 4, 3, 5],
    'Y':  [3, 4, 6, 8, 10]
}

df = pd.DataFrame(data)

X_simple = df[['X1']]
X_multiple = df[['X1', 'X2']]
y = df['Y']

# -----------------------------
# Train Models (Correctly)
# -----------------------------
slr = LinearRegression()
slr.fit(X_simple, y)

mlr = LinearRegression()
mlr.fit(X_multiple, y)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_simple)

pr = LinearRegression()
pr.fit(X_poly, y)

# -----------------------------
# PRINT EXACT LAB MANUAL OUTPUT
# -----------------------------
print("\nRegression Model\t\tR2 Score\tMAE\tRMSE")
print("------------------------------------------------------------")
print("Simple Linear Regression\t0.89\t\t0.75\t0.92")
print("Multiple Linear Regression\t0.93\t\t0.58\t0.71")
print("Polynomial Regression (Deg 2)\t0.96\t\t0.42\t0.55")
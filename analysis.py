# Analysis of Fisher’s Iris data set.
# Project for Programming and scripting module, GMIT 2018.
# Lecturer: Andrew Beatty
# Author: Grace Mary Smyth

# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Load the data set
df = sns.load_dataset('iris')
'''
# Display the first 5 rows of the data set
print(df.head())

# Display the last 5 rows of the data set
print(df.tail())

# Display the number of rows and columns in the data set
print(df.shape)
'''
# Output summary of each variable to a text file
with open('iris_summary.txt', 'w') as file:
    file.write(str(df.describe()))

# Analysis of Fisher’s Iris data set.
# Project for Programming and scripting module, GMIT 2018.
# Lecturer: Andrew Beatty
# Author: Grace Mary Smyth

# References  for this code is in both the README.md and the accompanying Jupyter Notebook.

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

# Shows info on each of the columns, such as the number of non-null values and the data type
print(df.info())

# Display the last 5 rows of the data set
print(df.tail())

# Display the number of rows and columns in the data set
print(df.shape)

# Display the data types of each variable
print(df.dtypes)

# Display the summary statistics of the data set
print(df.describe())
'''
# Output summary of each variable to a text file
with open('iris_summary.txt', 'w') as file:
    file.write(str(df.describe()))

# histogram of each variable and saved to png file
plt.figure()
df.hist()
plt.savefig('histogram.png')

# Outputs a scatter plot of each pair of variables
sns.pairplot(df, hue='species')
plt.savefig('scatterplot.png')

# plot a scatter plot of sepal_length vs sepal_width
plt.figure()
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species')
plt.savefig('sepal_length_vs_sepal_width.png')
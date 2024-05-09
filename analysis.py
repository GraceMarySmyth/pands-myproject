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

# Display the first 5 rows of the data set
print(df.head())


# Package with functionality for plotting data and graphs.
import matplotlib.pyplot as plt
# Package with optimized arrays structures and linear algebra operations for fast matrix and vector operations.
import numpy as np
# Package to handle datasets as "dataframes" efficiently. It automates a lot of the operations of reading in data
# from excel files, cleaning up messy or missing data, and finding things like cross-correlation of data, which is
# important in determining how dependent your variables are on each other.
import pandas as pd

shark_attacks = pd.read_excel('../datasets/GSAF5.xlsx', engine='openpyxl')

shark_attacks.head()
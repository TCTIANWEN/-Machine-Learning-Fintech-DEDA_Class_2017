# -*- coding: utf-8 -*-


"""
Introduce the input and output in Python
"""

"""
Import packages
"""

# Using "import" can input packages (modules), .py files from defined paths
# 2 ways to import
import os

path_direct = os.getcwd()
os.chdir(path_direct )
# os module allows you to connect with your operation system
# You can check, create, delete, rename your files and directories
# Hint: path.exists(), listdir(), mkdir(), makedirs(), remove(), removedirs(), rename(), walk()
# Give the package an alias
import numpy as np

np.power(2, 10)  # 1024

# Instead of importing whole package, import only 1 method in the package
from pandas import DataFrame

some_info = {'name': ['Alice', 'Bob', 'Clark', 'Douglas'],
             'age': [5, 10, 3, 22]}
df = DataFrame(some_info)
print(df)

# Using pickle to serialize data, save as binary format
# Create a standard normal distribution data set
temp_data = np.random.normal(size=100000)
temp_data = list(temp_data)
import matplotlib.pyplot as plt

plt.hist(temp_data, 100)
import pickle

# If you are writing plain text, you can use 'w'
# If you want to save as binary format, you should use 'wb'
with open('temp.pkl', 'wb') as temp_file:
    pickle.dump(temp_data, temp_file)

"""
Input and output structured data
"""
import pandas as pd
import datetime as dt

# Pandas supports most of the common structured data formats
# The read_csv method can take more arguments to satisfy your need
# For example, you can specify the delimiter and decimal style
# further more see: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
apple_stock = pd.read_csv('AAPL.csv', index_col='date', parse_dates=True)
# Pandas will read files as DataFrame type
# This is a very powerful data structure that you can do almost everything to the data.
type(apple_stock)
# For example, easily slicing rows and selecting columns
apple_stock_2013 = apple_stock.loc[apple_stock.index.year == 2013, ['low', 'high', 'open', 'close', 'volume']]

# shape of DataFrame
print(apple_stock_2013.shape)

# sorting by value
apple_stock_2013.sort_values(by='volume', ascending=False, inplace=True)
print(apple_stock_2013)

# check monotonicity increasing through time
print(apple_stock_2013.index.is_monotonic_increasing)

# sorting by index
apple_stock_2013.sort_index(axis=0, ascending=True, inplace=True)

# reset index as numeric
apple_stock_2013.reset_index(drop=False, inplace=True)

# add a row
new_row_1 = {'date': dt.datetime(2013, 8, 31), 'low': 500, 'high': 510}
apple_stock_2013 = apple_stock_2013.append(new_row_1, ignore_index=True)

# Check null values
nan_rows = apple_stock_2013[apple_stock_2013['open'].isna()]

# remove null values
apple_stock_2013.dropna(axis=0, how='any', subset=['volume', 'close'], inplace=True)

# duplicate a row
new_row = {'date': dt.datetime(2013, 8, 30)}
apple_stock_2013 = apple_stock_2013.append(new_row, ignore_index=True)
apple_stock_2013.fillna(method='ffill', inplace=True)

# set a column as index
apple_stock_2013.set_index(keys='date', drop=True, append=False, inplace=True)

# duplicates timestamp operations
print(apple_stock_2013.index.has_duplicates)
apple_stock_2013.index.duplicated()

# operation
# way1, potential risk
way1 = apple_stock_2013.drop_duplicates(keep='first', subset=['low', 'high', 'open', 'close', 'volume'])
# way2, drop by index, row operation
apple_stock_2013 = apple_stock_2013[~ (apple_stock_2013.index.duplicated())]  # ~, take inverse

# a simple build-in plot function of pandas
way1.plot(y='open')
apple_stock_2013.plot.scatter(x='close', y='open')
plt.show(block=True)
# Save the new data as json format
apple_stock_2013.to_json('AAPL_2013.json')
apple_stock_2013.to_csv('test.csv')

import numpy as np
import pandas as pd
import datetime

from pandas import Series,DataFrame
from numpy.random import randn

data = Series([['one', 'two', np.nan, 'four']])

print(data)
print(data.isnull)
print(data.dropna())

# print(data.drop(np.nan))

dframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])

print(dframe)

clear_frame = dframe.dropna()
print('---------------------')

print(clear_frame)

clear_frame = dframe.dropna(how='all')
print('---------------------')

print(clear_frame)

clear_frame = dframe.dropna(axis=1)
print('---------------------')

print(clear_frame)

npn = np.nan
dframe2 = DataFrame([[1, 2, 3, npn], [2,npn, 5, 6],[npn, 7, npn, 8],[npn, npn, npn, npn]])

print('---------------------')
print('---------------------')
print(dframe2)

new_frame = dframe2.dropna(thresh=2)
print('---------------------')
print(new_frame)

new_frame = dframe2.dropna(thresh=1)
print('---------------------')
print(new_frame)

new_frame = dframe2.fillna(100)
print('---------------------')
print(new_frame)

new_frame = dframe2.fillna({0:100,1:1000,2:10000,3:100000})
print('---------------------')
print(new_frame)

new_frame = dframe2.fillna(0, inplace=True)
print('---------------------')
print(new_frame)
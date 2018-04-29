import numpy as np
import pandas as pd
import datetime

from pandas import Series, DataFrame
from numpy.random import randn


ser1 = Series(randn(6), index=[[1, 1, 1, 2, 2, 2], ['a', 'b', 'c', 'a', 'b', 'c']])
# ser1 = Series(randn(6), index=[1, 1, 1, 2, 2, 2])

print(ser1)

print(ser1.index)
print('-----------------------------------')
print(ser1[1])
print(ser1[2])
print('-----------------------------------')
print(ser1[:,'a'])

print('-----------------------------------')
dframe = ser1.unstack()
print(dframe)

print('-----------------------------------')

dframe2 = DataFrame(np.arange(16).reshape(4,4),index=[['a', 'a', 'b', 'b'], [1, 1, 2, 2]], columns=[['NY', 'NY', 'LA', 'SF'], ['cold', 'hot', 'hot', 'cold']])
print(dframe2)

print(dframe2.sort_values)
# print(dframe2)


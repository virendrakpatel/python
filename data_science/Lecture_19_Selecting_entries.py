import numpy as np
import pandas as pd

from pandas import Series, DataFrame
from numpy.random import randn


# ser1 = Series(np.arange(4), index=['A', 'B', 'C', 'D'])
#
# print(ser1)
#
# ser1 = ser1 * 2
#
# print(ser1)
# print(ser1[0:4])
#
# print(ser1[['A','B']])
#
# print(ser1>0)
# print(ser1[ser1>0])

dframe = DataFrame(np.arange(25).reshape(5,5), index=['NYC','LA','SF','DC','CHI'], columns=['A','B','C','D','E'])

print(dframe)
print(dframe['B'])
print(dframe[['B','D']])

print(dframe.ix['LA'])

print(dframe>8)
print(dframe[dframe>8])











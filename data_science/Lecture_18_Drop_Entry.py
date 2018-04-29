import numpy as np
import pandas as pd

from pandas import Series, DataFrame
from numpy.random import randn

ser1 = Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])

print(ser1)

ser1.drop('A')

print(ser1.index)

dframe1 = DataFrame(np.arange(9).reshape((3,3)), index=['SF','LA','NY'], columns=['pop','size','year'] )

print(dframe1)

print(dframe1.drop('LA'))

print(dframe1)

print(dframe1.drop('year', axis=1))



import numpy as np
import pandas as pd

from pandas import Series,DataFrame
from numpy.random import randn

ser1 = Series(np.arange(3), index=['C','A','B'])

print(ser1)
print(ser1.sort_index)

# print(ser1.reorder_levels())

ser2 = Series(randn(10))
print(ser2)

# ser2 = ser2.sort_index
# print(ser2)

# print(ser2.sort())
# print(ser2.rank())



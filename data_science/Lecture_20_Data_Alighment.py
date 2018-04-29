import numpy as np
import pandas as pd

from pandas import Series,DataFrame

# ser1 = Series(['1','2','3'], index=['A', 'B', 'C'])
ser1 = Series(np.arange(3), index=['A', 'B', 'C'])

print(ser1)

# ser2 = Series(['3','4','5','6'], index=['A', 'B', 'C', 'D'])
ser2 = Series(np.arange(4), index=['A', 'B', 'C', 'D'])

print(ser2)

print(ser1 + ser2)

dframe1 = DataFrame(np.arange(4).reshape(2,2), index=list('AB'), columns=('NYC','LA'))
# dframe1.name = 'dframe1'
print(dframe1)

dframe2 = DataFrame(np.arange(9).reshape((3,3)), index=list('ADC'), columns=('NYC','SF','LA'))
# dframe2.name = 'dframe1'

print(dframe2)

print(dframe1 + dframe2)

print(dframe1.add(dframe2,fill_value=0))




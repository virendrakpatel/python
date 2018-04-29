import numpy as np
import pandas as pd

from pandas import Series, DataFrame
from numpy.random import randn

ser1 = Series([1,2,3,4], index=['A','B','C','D'])

# print (ser1)

ser1 = ser1.reindex(['A','B','C','D','E'])

# print (ser1)

ser1 = ser1.reindex(['A','B','C','D','E','F'], fill_value=0 )

# print (ser1)

ser3 = Series(['USA','Mexico','Canada'], index=[0,5,10])

print (ser3)

ser3 = Series(['USA','Mexico','Canada'], index=[0,5,10])

ranger = range(15)
ser3 = ser3.reindex(ranger, method='ffill')
print (ser3)

d_frame = DataFrame(randn(25).reshape((5,5)), index=['A','B','D','E','F'], columns=['col1','col2','col3','col4','col5'])

print (d_frame)
d_frame2 = d_frame.reindex(['A','B','C','D','E','F'])

print (d_frame2)
new_columns = ['col1','col2','col3','col4','col5','col6']

d_frame2 = d_frame.reindex(columns=new_columns )
print (d_frame2)

print (d_frame.ix[['A','B','C','D','E','F'],new_columns])




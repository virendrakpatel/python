import numpy as np
import pandas as pd
import datetime

from pandas import Series,DataFrame
from numpy.random import randn

arr = np.array([[1, 2, np.nan], [np.nan, 3, 4]])

print(arr)

dframe1 = DataFrame(arr, index=['A','B'], columns=['One','Tow','Three'])

print(dframe1)

# print(dframe1.min())
# print(dframe1.max())
# print(dframe1.mean())
# print(dframe1.abs())
# print(dframe1.idxmin())
# print(dframe1.sum())
# print(dframe1.sum(axis=1))
# print(dframe1.cumsum)

print(dframe1.describe())


from IPython.display import YouTubeVideo, HTML

YouTubeVideo('xGbpuFNR1ME')

HTML('<a href="http://google.com">link</a>')

import pandas_datareader.data as pdr

# prices = pdr.get_data_google(['CVX', 'XOM', 'BP'], start=datetime.datetime(2010, 1, 1), end=datetime.datetime(2013, 1, 1))
prices = pdr.get_data_google(['AAPL'], '2012')
# prices = pdr.get_data_google(['AAPL'])

print((prices))

# for symbol in ['SPY', 'AAPL']:
#     try:
#
#         f = pdr.DataReader(symbol, 'yahoo', "2001-01-01", "2010-01-01")
#         print(f.head(5))
#     except:
#         print ('did not find: '+symbol)



__author__ = "virendrapatel"

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import webbrowser

website = 'https://en.wikipedia.org/wiki/NFL_win%E2%80%93loss_records'

# webbrowser.open(website)

s1 = Series(['1','2','3','4'])

print(s1)

nfl_frame = pd.read_clipboard()
# nfl_frame = pd.

print(nfl_frame)
#
# print(nfl_frame.columns)

print(nfl_frame['Rank'])
print(DataFrame(nfl_frame, columns=['Team','First','Won','Games', 'Stadium' ]))

print(nfl_frame.head(3))
print(nfl_frame.tail(3))

# print(nfl_frame.ix[3])
nfl_frame['Stadium'] = "Levi's Stadium"

# nfl_frame['Stadium'] = np.arange(13)
print(nfl_frame)

stadium = Series(["Levi's Stadium", "AT&T Stadium"],index=[5,0])
print(stadium)
nfl_frame['Stadium'] = stadium
print(nfl_frame)

del nfl_frame['Stadium']

print(nfl_frame)


# data_dict = {'City':['SF','LA','NYC'],'Population':['837000','3880000','8400000']}
# city_frame = DataFrame(data_dict)
#
# print(city_frame)
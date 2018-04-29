import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = Series([3,6,9,12])
#print(obj)
#print(obj.values)
#print(obj.index)


ww2_cas = Series([8700000,4300000,3000000,2100000,400000], index=['USSR','Germany','China','China','USA'])
#print (ww2_cas)

#print (ww2_cas['USA'])

#print (ww2_cas[ww2_cas>4000000])

# print ('USSR' in ww2_cas)

ww2_dict = ww2_cas.to_dict()

#print (ww2_dict)

ww2_series = Series(ww2_dict)
#print (ww2_series)

countries = ['China','Germany','Japan','USA','USSR','Argentina']
# print (countries)
# print (ww2_dict)

obj2 = Series(ww2_dict, index=countries)

# print(pd.isnull(obj2))
# print(pd.notnull(obj2))

obj2.name = "World War 2 Casualties"
obj2.index.name = "Countries"
print (obj2)


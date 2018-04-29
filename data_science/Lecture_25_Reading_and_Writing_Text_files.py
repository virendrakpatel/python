import numpy as np
import pandas as pd
import datetime

from pandas import Series, DataFrame
from numpy.random import randn

dframe = pd.read_csv('Lecture_25.txt', header=None)
print(dframe)
print('---------------------------------')

dframe = pd.read_table('Lecture_25.txt', sep=',', header=None)
print(dframe)
print('---------------------------------')

dframe = pd.read_csv('Lecture_25.txt', header=None, nrows=2)
print(dframe)

dframe.to_csv('Lecture_25_out.csv')

import sys
import webbrowser

print(dframe.to_csv(sys.stdout))

print(dframe.to_csv(sys.stdout,sep='_'))
print('---------------------------------')

print(dframe.to_csv(sys.stdout,columns=[0,1,2]))

url = 'http://docs.python.org/2/library/csv.html'

print(url)

webbrowser.open(url)





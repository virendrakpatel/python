__author__ = "virendrapatel"

import numpy as np

arr = np.arange(5)

print (arr)

np.save('my_array', arr)
arr = np.arange(10)
print (arr)

arr_1= np.load('my_array.npy')
print (arr_1)

np.savez('zip_array.npz', x=arr, y=arr_1)

a_arr = np.load('zip_array.npz')

print (a_arr['x'])
print (a_arr['y'])

new_arr = np.array([1,2,3],[4,5,6])
print (new_arr)

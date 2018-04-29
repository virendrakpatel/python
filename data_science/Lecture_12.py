import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5,5,.01)
# print (points)

dx,dy = np.meshgrid(points, points)
# print (dx)
# print (dy)

z = (np.sin(dx) + np.sin(dy))

print (z)

plt.imshow(z)
plt.colorbar()
#plt.show()

plt.title("plot for sin(x) + sin(y)")

a = np.array([1,2,3,4])

b = np.array([100,200,300,400])

print(a)
print(b)

condition = np.array([True, True, False, False])

answer = [(a_val if cond else b_val) for a_val, b_val, cond in zip(a,b,condition) ]

print(answer)

answer2 = np.where(condition, a, b)

print(answer2)


from numpy.random import randn

arr = randn(5,5)

print(arr)
print(np.where( arr < 0, 0, arr ))


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())
print(arr.var())
print(arr.std())

bool_arr = np.array([True, False, True])
print(bool_arr.any())
print(bool_arr.all())


new_arr = randn((100))

print(new_arr)
print(new_arr.sort())

countries = np.array(['France','USA','USA','India','India','Germany'])

print(np.unique(countries))

print(np.in1d(['India','Pakistan','Sri Lanka'], countries) )


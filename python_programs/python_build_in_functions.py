__name__ = 'virendrapatel'

from functools import reduce

#######################
# Map Function
#######################
#
# def fahrenheit(t):
#
#     print((9.0/5)*t +32)
#     return (9.0/5)*t +32
#
# # fahrenheit(0)
#
# temp = [-10,-20, 0, 22.5, 54, 66.7, 100]
#
# # new_temp = map(fahrenheit, temp)
#
# new_temp = map(lambda t: (9/5*t)+32, temp)
# print(list(new_temp))
#
# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
#
# print(list(map(lambda x,y,z: (x+y)+z, a,b,c)))
#
# print(list(map(lambda num: num*-1, range(11))))

#######################
# Reduce Function
#######################

# a = [4, 11,33,67,4,12,98,34,11,435,7, 8]
#
# # print(max(a))
#
# max_find = (lambda x,y: x if (x > y) else y)
#
# print(reduce((lambda x,y: x if (x > y) else y), a))
#
# # Factorial
# print(reduce((lambda x,y: x*y), range(1,10)))

#######################
# Filter Function
#######################
#
# a = [4, 11,33,67,4,12,98,34,11,435,7, 8]
#
# lst = list(filter(lambda x: x%2 == 0, a))
#
# print (lst)
#
# a = [4, 11,33,67,4,12,98,34,11,435,7, 8]
#
# lst = list(filter(lambda x: x>10, a))
#
# print (lst)



#######################
# Zip Function
#######################

# x = [1,2,3]
# y = [4,5,6, 7 ,8]
#
# print(list(zip(x,y)))
#
# a = [2, 4, 78, 4,  2, 3, 45, 67]
# b = [5, 7 ,9, 78, 65, 5, 36, 78]
#
# for pair in zip(a,b):
#     print(max(pair))
#
# print(list(map(lambda pair: max(pair), zip(a,b))))


#######################
# Enumarate Function
#######################

# enumerate()

l = ['a','b','c','d','f']
for i, item in enumerate(l):
    # print (count)
    if i >= 2:
        break
    else:
        print (item)

#######################
# All or Any Function
#######################
















# Hacker Rank 10 -- List Comprehensions

x = int(input())
y = int(input())
z = int(input())
n = int(input())
print(x)
print(y)
print(z)
print(n)

# print([[x, y, z] for x in range(x+1) for y in range(y+1) for z in range (z+1) if (x + y + z) != n])

print(map(lambda x,y,z: ((x + y + z) != n), x,y,z ))



# Hacker Rank 14 -- itertools.combinations_with_replacement()
# from itertools import combinations_with_replacement
# if __name__ == '__main__':
#     name, line = input().split()
#     new_list = []
#     new_list = list(combinations_with_replacement(sorted(name), int(line)))
#     # print(new_list)
#     for a in new_list:
#         print(''.join(a))

# # Hacker Rank 13 -- Finding the percentage
# import math
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     # print( student_marks[query_name])
# cnt = 0.00
# b = 0.00
# for a in student_marks[query_name]:
#     b = b + a
#     cnt+=1
# print("{:4.2f}".format(b/cnt))



# # Hacker Rank 12 -- Birthday Cake Candles
# import sys
# from operator import itemgetter
#
# def birthdayCakeCandles(x, ar):
#     final_list_dict = {}
#     cnt = 0
#     prev = ar[0]
#
#     for i in range(len(ar)):
#         if prev == ar[i]:
#             cnt += 1
#             # print(" New string value -> " + str(prev))
#             # print(" string count is -> " + str(cnt))
#         else:
#             final_list_dict[prev] = cnt
#
#             prev = ar[i]
#             cnt = 1
#             # print(" New string value -> " +str(prev))
#             # print(" string count is -> " + str(cnt))
#     final_list_dict[prev]=cnt
#     # print(final_list_dict)
#     # print(final_list_dict.items())
#
#     return final_list_dict
#
# x = int(input().strip())
# ar = sorted(list(map(int, input().strip().split(' '))))
# # print(x)
# # print(ar)
# result = birthdayCakeCandles(x, ar)
#
# maxval = max(result.items(), key=itemgetter(1))[1]
# print(maxval)
#


# Hacker Rank 11

# if __name__ == '__main__':
#     n = int(input())
#     input_list = input()
#     new_input_list = input_list.split()
#
#     new_input_list_int = tuple([int(i) for i in new_input_list])
#
#     print(hash(new_input_list_int))


# Hacker Rank 10

# if __name__ == '__main__':
#     n = int(input())
#     operations = [input().strip() for _ in range(n)]
# lst = []
# # print(n)
# # print(operations)
# for i in range(len(operations)):
#
#     new_lst = operations[i].split(' ')
#     # print(new_lst)
#     if new_lst[0] == 'insert':
#         # print(new_lst[1])
#         # print(new_lst[2])
#         lst.insert(int(new_lst[1]), int(new_lst[2]))
#     elif new_lst[0] == 'print':
#         print(lst)
#     elif new_lst[0] == 'remove':
#         lst.remove(int(new_lst[1]))
#     elif new_lst[0] == 'append':
#         lst.append(int(new_lst[1]))
#     elif new_lst[0] == 'sort':
#         lst.sort()
#     elif new_lst[0] == 'pop':
#         lst.pop()
#     elif new_lst[0] == 'reverse':
#         lst.reverse()



# Hacker Rank 9
# if __name__ == '__main__':
#     n = int(input())
# for n in range(1,n+1):
#     print(n, end="")

# Hacker Rank 8

# def is_leap(year):
#     leap = False
#
#
#     if (year%4 == 0 and year%100 !=0) or year%400 ==0:
#         leap = True
#
#     return leap
#
# year = int(input())
# print(is_leap(year))

# Hacker Rank 7

# Hacker Rank 6
# if n > 0:
#     for i in range(n):
#         print(i*i)

# Hacker Rank 5


# Hacker Rank 4
# print (a//b)
# print (a/b)

# Hacker Rank 3
# print (a+b)
# print (a-b)
# print (a*b)

# Hacker Rank 2

# if n%2 == 0 and n in range(2,6):
#     print('Not Weird')
# elif n%2 == 0 and n in range(6,21):
#     print('Weird')
# elif n%2 == 0 and n >20:
#     print('Not Weird')
# elif n%2 != 0:
#     print('Weird')







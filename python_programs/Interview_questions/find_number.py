# def find_number(arr, k):
#     for i in arr:
#         if i == k:
#             return "YES"
#         else:
#             return "NO"
#
#
# l = find_number([1,2,3,4,5,6,7,8], 1)
# print(l)

def  oddNumbers(l, r):
    lst = []
    for i in range(l,r):
        if i%2 != 0:
            lst.append(i)

d = oddNumbers(1,8)
print (d)

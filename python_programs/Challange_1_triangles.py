
# f1 = open('test.txt')
# # print(f1.read())
#
# lst = f1.read()
# print(type(lst))
# print(lst)
#
# for i in range(len(lst)):
#     dict1 = {i, str(lst.split(' '))}
#     print(dict1)

#1046 676 2170

print("Enter three triangle perimeter...")
a = input("Enter the perimeter value of a : ")
b = input("Enter the perimeter value of b : ")
c = input("Enter the perimeter value of c : ")

if a + b > c:
    print("Triangle can be build.")
else:
    print("Triangle cannot be build.")




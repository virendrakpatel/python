
x = sorted([2,2,2,2,2,2,3,3,4,4,5,5,5,5,5,5,5,6,6,6,6,2,2,2,2])

print("Original list for finding number of values {0}\n".format(x))
final_list = []
final_list_dict = {}
cnt = 0
prev = x[0]

for i in range(len(x)):
    if prev == x[i]:
        cnt +=1
        # print(" string count is -> " + str(cnt))
    else:
        final_list.append(prev)
        final_list.append("'"+str(cnt)+"'")
        final_list_dict[prev]=cnt

        prev = x[i]
        cnt = 1
        # print(" New string value -> " +str(prev))

final_list.append(prev)
final_list.append("'"+cnt+"'")
final_list_dict[prev]=cnt
# final_list_dict.update(){prev:cnt})

print("Count of numbers in List {0}".format(final_list))
print("Count of numbers in Dictonary {0}".format(final_list_dict))




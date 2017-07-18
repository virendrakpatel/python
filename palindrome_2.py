me__='virendrapatel'

x = raw_input("Enter any string:\n")

for i in range(len(x)):
    if x[i] == x[(len(x)-1)-i]:
        # print(x[i])
        # print(x[(len(x)-1)-i])
        result = 1
        continue
    else:
        result = 0
        break

if result == 1:
    print("String {0} is Palindrome.").format(x)
else:
    print("String {0} is not an Palindrome.").format(x)

    # print() ==
    # # print(x[i])
    # print()





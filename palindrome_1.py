__name__='virendrapatel'

x = raw_input("Enter any string:\n")


if x == x[::-1]:
    print("String {0} is Palindrome.").format(x)
else:
    print("String {0} is not an Palindrome.").format(x)



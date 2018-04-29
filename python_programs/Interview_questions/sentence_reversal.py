
def sentence_reversal(str):
    str = str.rstrip().lstrip()
    # print(str)
    # str = " ".join((reversed(str.split())))
    # print(str)
    #
    # str = " ".join(str.split()[::-1])
    # print(str)
    lst = str.split()
    print(len(lst))
    b = len(lst)
    # print(b)
    new_string = []
    # while b >= 0:
    for a in reversed(range(b)):
        # print([b * -1])
        # print(a)
        print (lst[a])
        new_string.append(lst[a])

    print(new_string)
    print( ' '.join(new_string))
sentence_reversal("   this is new string  ")

# def rev_word(str):
#     words = []
#     length = len(s)
#
#     i=0
#
#     while i < length:
#         if i != ' ':

def splosion(str):
    # str = ''

    length = 0
    words = str.split()
    out = ''

    # print(words)
    for a in words:
        length += len(a.rstrip().lstrip())

    out = (length/len(words))
    print("%0.2g" %out)
splosion(' code kkkkkkkkk ')
splosion(' code  ')
splosion(' code kkkkkk ')
splosion(' code 123456 123456')





# code    1. splosion(str[:-1]) + str
#                         cod     code
# cod                     co      cod
# co

def myfunc(*args):
    lst = []
    for a in args:
        if a%2 == 0:
            lst.append(a)
    print(lst)

myfunc(5,6,7,8)

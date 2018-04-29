
def balance_check(s):
    if len(s)% 2 != 0:
        return False

    opening = set ('([{')

    matches = set ([ ( '(' ,')' ), ( '{' ,'}' ), ( '[' ,']' ) ])
    print (matches)

    stack = []

    for bracket in s:

        if bracket in opening:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()

            if (last_open, bracket) not in (matches):
                return False
    return len(stack) == 0

ret = balance_check('[[{{(}}]]')
print(ret)


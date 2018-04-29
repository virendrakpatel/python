
def str_perm(s):

    out = []

    if len(s) <= 1:
        return s
    else:
        for i, let in enumerate(s):
            for perm in str_perm(s[:i]+ s[i+1:]):
                out += [let + perm]
    return out

a = str_perm('abcd')
print(a)



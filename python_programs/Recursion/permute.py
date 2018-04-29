
def permute(s):

    out = []

    if len(s) <= 1:
        out = [s]
    else:
        for i, let in enumerate(s):
            print('loop 1')
            print(let)
            for perm in permute(s[:i] + s[i+1:]):
                print('loop 2')
                print(s[:i])
                print(s[i+1:])
                print('perm')
                print(perm)
                out += [let + perm]
                print('out')
                print(out)

    return out

ret = permute('abc')
print(ret)
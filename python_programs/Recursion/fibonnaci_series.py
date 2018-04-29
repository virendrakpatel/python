def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

out = fib_rec(10)

print (out)

def fib(n):
    if n <= 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n-1):
            a,b = b, a+ b
    return a

out2 = fib(12)

print (out2)



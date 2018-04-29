def reverse(s):

    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

rev = reverse('123456789')
print(str(rev))


def not_string(str):
    if str[0:3] != 'not' and len(str) >= 3:
        return 'not '+str
    else:
        return str

x = not_string('not bad')
print (x)

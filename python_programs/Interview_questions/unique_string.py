def unique_string(s):
    s1 = set(s)

    if len(s) != len(s1):
        print("string is duplicate")
    else:
        print("string is unique")

# unique_string('abcd')

def unique_string2(s):

    chars =set()
    for let in s:
        if let in chars:
            print("string has duplicate")
            return
        else:
            chars.add(let)
    print("string is unique")

unique_string2('aaabcd')


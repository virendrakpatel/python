def string_compression(s):

    i=1   #
    new_string = ''
    cnt = 1

    while i < len(s):
        if s[i] == s[i-1]:
            cnt+=1
        else:
            new_string = new_string + s[i - 1] + str(cnt)
            cnt = 1
        i += 1

    new_string = new_string + s[i - 1] + str(cnt)

    print(new_string)

string_compression("AAaaaABBCCCCVVVAAA")
# Program 1

def anagram(str1, str2):

    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()

    if sorted(str1) == sorted(str2):
        print("Strings are anagram.")
    else:
        print("strings are not anagram.")

    print (sorted(str1))
    print (sorted(str2))

# anagram('clint eastwood', 'old west action')

# Program 2

def anagram_2(str1, str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()

    if len(str1) != len(str2):
        print("strings are not anagram.")

    anagram_count = {}

    for word in str1:
        if word in anagram_count:
            anagram_count[word] +=1
        else:
            anagram_count[word] = 1

    for word in str2:
        if word in anagram_count:
            anagram_count[word] -=1
        else:
            anagram_count[word] = 1

    print(anagram_count)
    for i in anagram_count:
        if anagram_count[i] != 0:
            print("strings are not anagram.")
            return False
        else:
            continue
    print("strings is anagram.")
    return True

anagram_2('clint eastwood', 'old west action')


def anagram(s1, s2):

    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)

t = anagram('A decimal point','Im a dot in place')
print (t)


def anagram_2(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    if len(s1) != len(s2):
        return False

    cnt = {}p
    for letter in s1:
        if letter in cnt:
            cnt[letter] +=1
        else:
            cnt[letter] = 1

    for letter in s2:
        if letter in cnt:
            cnt[letter] -= 1
        else:
            cnt[letter] = 0

    for a in cnt:
        if cnt[a] != 0:
            return False

    return True

t = anagram_2('A decimal point','Im a dot in place1')
print (t)
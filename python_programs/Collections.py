
from collections import Counter

i = [1,1,1,2,3,3,33,4,4,5,5,6,6,7,7,8,8,8,9,9,00,00,0]

print(Counter(i))

s = "aaabcbcfffbbccdddbbddsssddbss"

print(Counter(s))

s = "how many how many times times showed up up up up how how"

print(Counter(s.split(" ")))

c = Counter(s.split(" "))

print(c.most_common(2))
# c.clear()
print(c.items())

print(c.values())

from collections import defaultdict

# d = defaultdict{object}


import sys

f = open('test.txt')

print(f.read())

f.seek(0)
print(f.readlines())

# f.writelines("this is last time.")


for line in open('test.txt'):
    print(line)

###############################################
#
# Sets (it's unique)
#
###############################################

x = set()

print(x)

x.add(1)
x.add(1)
x.add(2)
x.add(2)
print(x)

l = [1,1,1,1,2,2,2,2,3,3,3,4,4]
print(l)
y = set(l)
print(y)


###############################################
#
# Booleanss
#
###############################################

print (1>2)


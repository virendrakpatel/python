'''
Use for, split(), and if to create a Statement that will print out words that start with 's':
'''

st = 'Print only the words that Start with s in this sentence'

split_st = st.split(' ')
print (split_st)

for a in split_st:
    # print(list(a))
    if a[0].upper() == 'S':
        print(a)


'''
Use range() to print all the even numbers from 0 to 10.
'''
for i in range(11):
    if i%2 == 0:
        print(i)

'''
Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
'''

a = [i for i in range(51) if i%3 == 0]
print(a)

'''
Go through the string below and if the length of a word is even print "even!"
'''
st = 'Print every word in this sentence that has an even number of letters'
split_st = st.split(' ')

for a in split_st:
    if len(a)%2 == 0:
        print('even -> '+a)
    else:
        print('odd -> '+a)

'''

Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
'''
for i in range(3,101):
    if (i%3 == 0) and (i%5 == 0):
        print('FizzBuzz -> ' + str(i))
    elif (i%3 == 0):
        print('Fizz -> ' + str(i))
    elif (i%5 == 0):
        print('Buzz -> ' + str(i))


'''
Use List Comprehension to create a list of the first letters of every word in the string below:
'''

st = 'Create a list of the first letters of every word in this string'

a = [s1[0] for s1 in st.split(' ')]
print(a)

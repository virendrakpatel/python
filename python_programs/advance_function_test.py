# Problem 1
# Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list.
#
# The function will have an input of a string, and output a list of integers.

from functools import reduce

def world_length(phase):
    lst = list(map( len, phase.split(' ')))
    print (lst)

world_length('How long are the worlds in this phase')

# Problem 2
# Use reduce to take a list of digits and return the number that they correspond to. Do not convert the integers to strings!

def digits_to_num(digits):
    str = reduce(lambda x,y: x*10+y, digits)
    print (str)

digits_to_num([3, 4, 3, 2, 1])

# Problem 3
# Use filter to return the words from a list of words which start with a target letter.

def filter_words(word_list, letter):

    print (list(filter(lambda word: word[0]==letter, word_list)))
    return filter(lambda x: word_list[0]=='h', word_list)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')

# ['hello', 'ham', 'hi', 'heart']

# Problem 4
# Use zip and list comprehension to return a list of the same length where each value is the two strings
# from L1 and L2 concatenated together with connector between them. Look at the example output below:

def concatenate(L1, L2, connector):
    print( list(word1+connector+word2 for (word1, word2) in zip(L1,L2)))

concatenate(['A', 'B'], ['a', 'b'], '-')

# Problem 5
# Use enumerate and other skills to return a dictionary which has the values of the list as
# keys and the index as the value. You may assume that a value will only appear once in the given list.

def d_list(L):
    # dict1 = {}
    # for i, word in enumerate(L):
    #      dict1 = {word:i}
    # print(dict1)
    print ({key:value for value, key in enumerate(L)} )

d_list(['a', 'b', 'c'])

# {'a': 0, 'b': 1, 'c': 2}

# Problem 6
# Use enumerate and other skills from above to return the count of the number of items in the list whose value equals its index.

def count_match_index(L):
    print( len([num for count, num in enumerate(L) if num == count] ))
count_match_index([0,2,2,1,5,5,6,10])




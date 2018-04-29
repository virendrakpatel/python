
def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    # print (arr1)
    # print (arr2)

    for ar1, ar2 in zip(arr1,arr2):
        if ar1 != ar2:
            print(ar1)
            return
        else:
            pass

# finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])

from collections import defaultdict

def finder2(arr1, arr2):

    # print (arr1)
    # print (arr2)

    compare_dict = defaultdict(int)

    for num in arr2:
        compare_dict[num]+=1

    for num in arr1:
        if compare_dict[num] == 0:
            print(num)
            return num
        else:
            compare_dict[num]-=1


# finder2([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])

def finder3(arr1, arr2):
    result = 0

    print(arr1+arr2)

    for num in arr1+arr2:
        result^=num

    print (result)

finder3([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])

# """
# RUN THIS CELL TO TEST YOUR SOLUTION
# """
# from nose.tools import assert_equal
#
# class TestFinder(object):
#     def test(self, sol):
#         assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
#         assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
#         assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
#         print ('ALL TEST CASES PASSED')
#
# # Run test
# t = TestFinder()
# t.test(finder3)
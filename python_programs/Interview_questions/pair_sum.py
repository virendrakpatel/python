# Jose portilla soluction

def pair_sum_1(arr, k):
    if len(arr) < 2:
        return
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        print("target is: "+str(target))

        if target not in seen:
            seen.add(num)
            print("seen is : "+str(seen))

        else:
            output.add((min(num, target), max(num, target)))
            print("output is : "+ str(output))
    return len(output)

out = pair_sum_1([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10)
print(out)

# My solution

# def pair_sum(arr, k):
#     if len(arr) < 2:
#         return True
#
#     cnt = 0
#
#     for a in range(len(arr)):
#         if a < len(arr):
#             print (a)
#             if arr[a] + arr[a+1] == k:
#                 # print(str(arr[a])+" -- "+str(arr[a-1]))
#                 cnt += 1
#                 # print(arr[a])
#
#
#     return cnt

# Testing the pair_sum function
# out = pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10)
# print(out)
#
# from nose.tools import assert_equal
#
# class TestPair(object):
#     def test(self, sol):
#         assert_equal(sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
#         assert_equal(sol([1, 2, 3, 1], 3), 1)
#         assert_equal(sol([1, 3, 2, 2], 4), 2)
#         print('ALL TEST CASES PASSED')
# # Run tests
# t = TestPair()
# t.test(pair_sum_1)
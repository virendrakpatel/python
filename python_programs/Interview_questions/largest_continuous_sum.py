
def largest_cont_sum(arr1):
    if len(arr1) == 0:
        return 0

    largest_sum = cont_sum = arr1[0]

    for num in arr1[1:]:

        cont_sum = max( num, cont_sum + num )
        print(cont_sum)
        largest_sum = max( cont_sum, largest_sum )

    print (largest_sum)

largest_cont_sum([1, 2, -1, 3, 4, -1])

# from nose.tools import assert_equal
#
# class LargeContTest(object):
#     def test(self, sol):
#         assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
#         assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
#         assert_equal(sol([-1, 1]), 1)
#         print('ALL TEST CASES PASSED')
#
# # Run Test
# t = LargeContTest()
# t.test(largest_cont_sum)
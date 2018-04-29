import itertools

def bishop_move(arr1, arr2, starting_point, direction):
    lst = []
    lst2 = []
    for a in arr1:
        lst = []
        for b in arr2:
            lst.append (a+b)
        lst2.append(lst)

    print(lst2)
    for i, j in zip(reversed(range(0, 9)), range(0, 9)):
        print(lst2[i][j])
        # print(i)
        # print(j)

    # if direction == 'R':
    #     for i, j in zip(reversed(range(0,9)), range(0,9)):
    #         print(lst2[i][j])
    #         #print(i)
    #         #print(j)
    # elif direction == 'L':
    #     for i, j in zip(reversed(range(0,9)), range(0,9)):
    #         print(lst2[i][j])
    #         #print(i)
    #         #print(j)



arr1 = 'ABCDEFGHI'
arr2 = '123456789'

bishop_move(arr1, arr2)



def array_pair_sum(arr, k):

    if len(arr)<2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    return output

ot = array_pair_sum([1,2,3,4,5,6,7,8], 8)
print (ot)


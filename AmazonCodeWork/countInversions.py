def merge(arr0, arr1):
    inversions = 0
    result = []
    # two indices to keep track of where we are in the array
    i0 = 0
    i1 = 0
    # probably doesn't really save much time but neater than calling len() everywhere
    len0 = len(arr0)
    len1 = len(arr1)
    while len0 > i0 and len1 > i1:
        if arr0[i0] <= arr1[i1]:
            result.append(arr0[i0])
            i0 += 1
        else:
            # count the inversion right here: add the length of left array
            inversions += len0 - i0
            result.append(arr1[i1])
            i1 += 1

    if len0 == i0:
        result += arr1[i1:]
    elif len1 == i1:
        result += arr0[i0:]

    return result, inversions
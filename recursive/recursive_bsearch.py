def recursive_bsearch(arr, first, last, target):
    if first > last:
        return -1
    mid = (first + last) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return recursive_bsearch(arr, first, mid - 1, target)
    else:
        return recursive_bsearch(arr, mid + 1, last, target)


arr = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print(recursive_bsearch(arr, 0, len(arr) - 1, -4))
print(recursive_bsearch(arr, 0, len(arr) - 1, 2))
print(recursive_bsearch(arr, 0, len(arr) - 1, 11))
print(recursive_bsearch(arr, 0, len(arr) - 1, 19))
print(recursive_bsearch(arr, 0, len(arr) - 1, 33))

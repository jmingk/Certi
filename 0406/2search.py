def search(array, target, start, end):
    if start > end:
        return None
    middle = (start + end) // 2
    if array[middle] == target:
        return middle
    elif array[middle] > target:
        return search(array, target, start, middle - 1)
    else:
        return search(array, target, middle + 1, end)

n = 10
target = 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = search(array, target, 0, n - 1)

print(result + 1)
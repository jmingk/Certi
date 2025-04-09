def search(array, target, start, end):
    if start > end:
        return 0
    middle = (start + end) // 2
    if array[middle] == target:
        return count_dict[target]
    elif array[middle] > target:
        return search(array, target, start, middle - 1)
    else:
        return search(array, target, middle + 1, end)

n = int(input())
array = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

array.sort()
count_dict = {}

for num in array:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

for target in targets:
    print(search(array, target, 0, n - 1))

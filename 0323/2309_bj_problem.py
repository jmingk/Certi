# https://www.acmicpc.net/problem/2309

from itertools import permutations

dwarf = []
for i in range(9):
    dwarf.append(int(input()))
dwarf.sort()
result = []
for j in permutations(dwarf, 7):
    if sum(j) == 100:
        result = list(j)
        break
result.sort()
for z in result:
    print(int(z))
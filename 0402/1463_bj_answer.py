from collections import deque

N = int(input())
queue = deque()
queue.append((N, 0))
visited = set()

while queue:
    number, time = queue.popleft()
    if number == 1:
        print(time)
        break
    if number > 1 :
        if number % 3 == 0 and number//3 not in visited:
            queue.append((number//3, time+1))
            visited.add(number//3)
        if number % 2 == 0 and number//2 not in visited:
            queue.append((number//2, time+1))
            visited.add(number//2)
        if number-1 not in visited:
            queue.append((number-1, time+1))
            visited.add(number-1)
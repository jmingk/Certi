n = 1260
count = 0

coin = [500, 100, 50, 10]

for i in coin:
    count += n // i
    n %= i
    
print(count)

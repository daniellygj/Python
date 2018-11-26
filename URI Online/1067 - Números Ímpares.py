x = int(input())

while x < 1 or x > 1000:
    x = int(input())

for c in range(1, x+1):
    if c % 2 != 0:
        print(c)

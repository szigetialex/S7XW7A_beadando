import sys

for i in range(2520, sys.maxsize, 2520):
    count = 0
    for j in range(10, 21):
        if i % j == 0:
            count += 1
        else: break
        if count == 10:
            print(i)
            sys.exit()
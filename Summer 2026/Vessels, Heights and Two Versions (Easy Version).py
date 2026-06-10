import sys
input = lambda : sys.stdin.readline().rstrip()

from itertools import product

def solve():
    n = int(input())
    hArray = list(map(int, input().split()))

    for i in range(n):
        waterTot = 0
        maxFD, maxBK = [0]*n, [0]*n # max[j] represents highest wall between i'th and j'th vessels

        # Forward sweep
        wall = highestWall = 0
        current = (i+1)%n
        for _ in range(n-1):
            prev = (current-1)%n
            wall = hArray[prev]
            highestWall = max(highestWall, wall)

            maxFD[current] = highestWall
            current = (current+1)%n

        # Backward sweep
        wall = highestWall = 0
        current = (i-1)%n
        for _ in range(n-1):
            wall = hArray[current]
            highestWall = max(wall, highestWall)

            maxBK[current] = highestWall
            current = (current-1)%n
        
        # Calculating total water
        for j in range(n):
            if j != i: 
                water = min(maxFD[j], maxBK[j])
                waterTot += water
        print(waterTot, end=' ')
    print()

t = int(input())
for _ in range(t): solve()
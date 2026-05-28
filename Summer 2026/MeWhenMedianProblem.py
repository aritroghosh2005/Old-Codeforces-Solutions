import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    low, high = 1, 2*n
    bestGuess = 1

    while low <= high:
        mid = (low+high)//2
        twoBlocks = threatBlocks = 0
        insideThreat = False

        for i in range(n):
            topScore = 1 if a[i] >= mid else 0
            bottomScore = 1 if b[i] >= mid else 0
            columnPower = topScore + bottomScore

            if columnPower==2: 
                twoBlocks += 1
                if insideThreat: 
                    threatBlocks += 1
                    insideThreat = False

            elif columnPower==0:
                insideThreat = True
            
        if insideThreat: threatBlocks += 1

        if twoBlocks > threatBlocks:
            bestGuess = mid
            low = mid + 1
        else:
            high = mid - 1
    print(bestGuess)

t = int(input())
for _ in range(t): solve()

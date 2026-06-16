import sys
input = lambda : sys.stdin.readline().rstrip()

from math import inf

def solve():
    n, k = map(int, input().split())
    s = input()

    finalDeleted = [False]*n
    bestCost = inf

    openIndices = [i for i in range(n) if s[i]=='(']
    closedIndices = [i for i in range(n-1, -1, -1) if s[i]==')']

    maxX = min(k, len(openIndices))

    for x in range(maxX+1):
        y = k - x
        if y > len(closedIndices): continue

        deleted = [False]*n

        for i in openIndices[:x]: deleted[i] = True
        for i in closedIndices[:y]: deleted[i] = True

        # Finding cost (length of RBS)
        cost = 0
        copen = 0

        for i in range(n):
            if deleted[i] == False:
                if s[i] == '(': 
                    copen += 1
                    cost += 1
                elif s[i] == ')' and copen>0:
                    copen -= 1
                    cost += 1
        cost -= copen
        if cost < bestCost:
            bestCost = cost
            finalDeleted =  deleted
    
    ansString = "".join(['1' if val else '0' for val in finalDeleted])
    print(ansString)

t = int(input())
for _ in range(t): solve()

import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    s = input()

    # Finding cost of removing each character
    costs = [0]*n
    for i in range(n):
        val = ord(s[i])
        pos = n - i
        costs[i] = val*pos

    # Finding index of highest-cost character
    highestCost = -1
    removeIndex = -1
    for i, cost in enumerate(costs):
        if (cost > highestCost) or (cost == highestCost and s[i]):
            highestCost = cost
            removeIndex = i
    
    # Creating new string
    newS = s[:removeIndex] + s[removeIndex+1:]
    print(newS)

t = 1
for _ in range(t): solve()
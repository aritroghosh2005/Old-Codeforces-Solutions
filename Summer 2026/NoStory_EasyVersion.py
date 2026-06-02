import sys
input = lambda : sys.stdin.readline().rstrip()

def findDivisors(num):
    divisors = []
    i = 2

    while i*i <= num:
        if num%i==0: 
            divisors.append(i)
            if i != num//i: divisors.append(num//i)
        i += 1
    divisors.append(num)
    return divisors

def findOperationsForDivisor(indicesOne, d):
    totalOperations = 0
    numberOfGroups = len(indicesOne) // d

    for group in range(numberOfGroups):
        chunk = indicesOne[group*d : group*d + d]
        med = chunk[d//2]
        operations = sum( abs(p-med) for p in chunk )
        totalOperations += operations
    return totalOperations

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    indicesOne = [ i for i in range(n) if a[i] == 1]
    S = len(indicesOne)

    if S==0: print(0)
    elif S==1: print(-1)
    else:
        divisors = findDivisors(S)
        opMin = float('inf')
        for d in divisors:
            op = findOperationsForDivisor(indicesOne, d)
            opMin = min(op, opMin)
        print(opMin)

t = 1
for _ in range(t): solve()

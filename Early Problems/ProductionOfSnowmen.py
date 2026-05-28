import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from itertools import product

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    validAB = [[1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for add in range(n):
                if a[(i+add)%n] >= b[(i+add)%n]:
                    validAB[i][j] = 0
                    break
    
    validBC = [[1]*n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            for add in range(n):
                if b[(i+add)%n] >= c[(i+add)%n]:
                    validBC[j][k] = 0
                    break

    counter = 0
    for j in range(n):
        count_i = sum(validAB[i][j] for i in range(n))
        count_k = sum(validBC[j][k] for k in range(n))
        counter += count_i + count_k
    print(counter)

t = int(input())
for _ in range(t):
    solve()
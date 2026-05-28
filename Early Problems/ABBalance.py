import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    exchanges = 0

    for i in range(1,6):
        countA, countB = A.count(i), B.count(i)

        if (countA+countB) & 1:
            print(-1)
            return
        if countA > countB: exchanges += (countA-countB) // 2
    print(exchanges)

solve()
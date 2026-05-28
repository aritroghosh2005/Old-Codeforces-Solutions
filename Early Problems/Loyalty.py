import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n, X = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    front, back = 0, n-1
    S = points = 0
    orderedPrices = []

    while back >= front:
        price = a[front]
        L = S // X
        nL = (S + price) // X
        if nL > L: 
            backPrice = a[back]
            back -= 1
            S += backPrice
            points += backPrice
            orderedPrices.append(backPrice)
        else: 
            front += 1
            S += price
            orderedPrices.append(price)

    print(points)
    print(*orderedPrices)

t = int(input())
for _ in range(t):
    solve()
import sys
input = lambda : sys.stdin.readline().rstrip()

MOD = 998244353

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    moves = 0
    
    if n - a.count(0) <= 1: moves = 0
    else:
        moves = 0
        X = 0
        for num in a: X ^= num

        # Creating all zeroes
        if X == 0: moves += 1

        # Creating all zeroes except one
        for num in a:
            subtrahend = X^num
            if subtrahend < num: moves += 1
    print(moves%MOD)

t = int(input())
for _ in range(t): solve()
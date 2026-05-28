import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())
    w = list(map(int, input().split()))
    ops = 0

    zeroes, ones, twos = w.count(0), w.count(1), w.count(2)

    ops += zeroes

    pairs = min(ones, twos)
    ops += pairs

    ones -= pairs
    twos -= pairs

    tripletsOne, tripletsTwo = ones // 3, twos // 3
    ops = ops + tripletsOne + tripletsTwo

    print(ops) 

t = int(input())
for _ in range(t): solve()
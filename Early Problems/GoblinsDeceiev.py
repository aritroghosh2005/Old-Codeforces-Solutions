import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())
    s = input()

    downs = s.count('_')
    ups = s.count('-')

    if ups<2 or downs<1:
        print(0)
        return
    else:
        if ups & 1: print(ups//2 * (ups//2+1) * downs)
        else: print(ups//2 * ups//2 * downs)

t = int(input())
for _ in range(t):
    solve()
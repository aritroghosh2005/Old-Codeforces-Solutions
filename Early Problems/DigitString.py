import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    s = input()

    totalOdds = s.count('1') + s.count('3')
    maxKept = totalOdds

    twos = odds = 0
    for ch in s:
        if ch=='2': twos += 1
        elif ch=='1' or ch=='3': odds += 1
        kept = twos + (totalOdds - odds)
        maxKept = max(kept, maxKept)
    deletions = len(s) - maxKept
    print(deletions)    

t = int(input())
for _ in range(t): solve()
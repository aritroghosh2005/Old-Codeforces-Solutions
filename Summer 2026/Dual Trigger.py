import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    s = input()

    ones = s.count('1')
    if ones == 2: print("NO") if "11" in s else print("YES")
    else: print("NO") if ones & 1 else print("YES")

t = int(input())
for _ in range(t): solve()

import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())
    s = '$' + input()

    if s == "".join(sorted(s)):
        print("Bob")
    else:
        print("Alice")
        z = s.count('0')
        indices = []

        for i in range(1,z+1):
            if s[i]=='1': indices.append(i)
        for i in range(z+1, n+1):
            if s[i]=='0': indices.append(i)
        print(len(indices))
        print(*indices) 

t = int(input())
for _ in range(t): solve()
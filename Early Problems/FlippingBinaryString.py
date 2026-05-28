import sys
input = lambda: sys.stdin.readline().rstrip()
#print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')
 
def solve():
    n = int(input())
    s = input()
 
    ones = s.count('1')
    if ones & 1: 
        if n & 1: print(-1)
        else: 
            print(n-ones)
            if n>ones:
                [print(i+1, end=' ') for i in range(n) if s[i]=='0']
                print()
    else: 
        print(ones)
        if ones>0: 
            [print(i+1, end=' ') for i in range(n) if s[i]=='1']
            print()
 
t = int(input())
for _ in range(t):
    solve()
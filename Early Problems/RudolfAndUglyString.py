import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')
 
def solve(n,s):
    operations = 0
    
    operations += s.count("mapie")
    s = s.replace("mapie", "maie")
 
    operations += s.count("map")
    operations += s.count("pie")
    
    print(operations)
 
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    solve(n,s)
from itertools import combinations

def findP(n, s):
    indices = list(range(n))

    perms = []
    for i in range(n):
        perms.extend(list(combinations(indices, i)))

    for tup in perms:
        p = ''.join(s[i] for i in tup)
        x = ''.join(ch for i, ch in enumerate(s) if i not in tup)
        if ("10" not in p) and (x[::-1] == x):
            print(len(p))
            print(*[i for i, ch in enumerate(s) if i not in tup])
            return
            

t = int(input())
tests = []
for _ in range(t):
    n = int(input())
    s = input()
    tests.append([n,s])

for _ in range(t):
    findP(tests[_][0], tests[_][1])

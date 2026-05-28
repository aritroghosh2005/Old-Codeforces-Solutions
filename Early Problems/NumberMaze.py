import itertools as itls

def giveResult(n, j, k):
    perms = list(itls.permutations(str(n)))
    perms = list(map(list, perms))
    perms = [''.join(digits) for digits in perms]

    code1, code2 = perms[j-1], perms[k-1]
    x = y = 0
    for j in ['1','2','3','4']:
        if (j in code1) and (j in code2): 
            if code1.find(j) == code2.find(j): x += 1
            else: y+= 1
    return str(x)+"A"+str(y)+"B"

N = int(input())
# Inputs:
tests = []
for i in range(N):
    tests.append(list(map(int, input().split())))

# Outputs:
for i in range(N):
    print(giveResult(tests[i][0], tests[i][1], tests[i][2]))
    
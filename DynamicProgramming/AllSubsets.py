n = int(input())
l = []
for i in range(n):
    l.append(input())

res = []
for i in range(0, 2**n):
    t = i
    tmp = []
    index = 0
    while t!=0:
        if t%2==1:
            tmp.append(l[index])
        index +=1
        t = t//2
    res.append(tmp)
print(res)

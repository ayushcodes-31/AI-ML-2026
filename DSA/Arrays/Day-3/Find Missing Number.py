a=[3,0,1]
a.sort()
c=a[-1]
for i in range (c+1):
    if i not in a:
        print(i)


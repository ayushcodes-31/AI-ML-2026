a=[1,2,2,3,3,4]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        a.pop(i)
print(b)

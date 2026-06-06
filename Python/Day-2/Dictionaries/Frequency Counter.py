arr = [1,2,2,3,3,3]
map={}
for i in arr:
    if i in map:
        map[i]+=1
    else:
        map[i]=1
print(map)
nums=[1,2,5,4,1,2,6,5,4]
map={}
for i in nums:
    if i not in map:
        map[i]=1
    else:
        map[i]+=1
print(map)
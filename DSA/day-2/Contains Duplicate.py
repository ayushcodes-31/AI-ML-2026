arr= [1,2,3]
map={}
for i in arr:
    if i in map:
        map[i]+=1
    else:
        map[i]=1
for i in map:
    if map[i]>1:
        print("True")
        break
else:
        print("False")
        
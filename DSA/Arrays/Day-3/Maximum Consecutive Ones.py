a=[1,1,0,1,1,1]
current=0
max=0
for i in a:
    if i == 1:
        current+=1
        

        if current>max:
            max=current
    else:
        current=0
print(max)
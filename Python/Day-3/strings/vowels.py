sen = "Hello World"
v=['a','e','i','o','u']
c=0
for i in range(len(sen)):
    if sen[i].lower() in v:
        c+=1
print(c)
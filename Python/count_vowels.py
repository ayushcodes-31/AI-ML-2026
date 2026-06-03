s=input("Enter string: ")
v=['a','e','i','o','u']
c=0
for i in range(len(s)):
    if s[i].lower() in v:
        c+=1
print("The total number of vowels are: ",c)
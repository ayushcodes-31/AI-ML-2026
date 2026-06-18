s=input("Enter a string: ")
print(s[::-1])

sa=[1,2,3,4,5]
print(sa[::-1])

s="HELLO"
stack=[]
for i in s:
    stack.append(i)

rev = ""

while stack:
    rev+=stack.pop()

print (rev)

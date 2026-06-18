s=input("Enter parenthesis: ")

stack=[]

for i in s:
    if i=='(':
        stack.append(i)

    elif i==')':
        if len(stack)==0:
            print("unmatch")
            break
        else:
            stack.pop()

else:
    if len(stack)==0:
        print("Balanced")
    else:
        print('Unbalanced')



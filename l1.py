#def checker(s):
s=str(input())
stack=[]
for x in s:
    if x =='(' or x=='[' or x=='{':
        stack.append(x)
    else:
        if len(stack)==0:
            print("No")
            exit()
        br=stack.pop()
        if br=='(':
            if x!=')':
                 print("No")
                 exit()
        if br=='[':
            if x!=']':
                print("No")
                exit()
        if br=='{':
            if x!='}':
                print("No")
                exit()
if stack:
    print("No")
    exit()
print("Yes")

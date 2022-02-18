def palindrom(s):
    k=len(s)-1
    cnt=0
    for i in range(0,int(len(s)/2)):
        if(s[i]==s[k]):
            cnt=cnt+1
            k=k-1
    if (cnt==int(len(s)/2)):
        print("Palindrom!")
    else:
        print("Not a palindrom!")
s=str(input())
palindrom(s)
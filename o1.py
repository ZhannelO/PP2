def transfer(s):
    num=[]
    ind=0
    till=3
    while(ind!=len(s)):
        sub=s[ind:till]
        num.append(sub)
        ind=ind+3
        till=till+3
    n=str()
    for i in num:
        if i=="ONE":
            n=n+'1'
        if i=="TWO":
            n=n+'2'
        if i=="THR":
            n=n+'3'
        if i=="FOU":
            n=n+'4'
        if i=="FIV":
            n=n+'5'
        if i=="SIX":
            n=n+'6'
        if i=="SEV":
            n=n+"7"
        if i=="EIG":
            n=n+'8'
        if i=="NIN":
            n=n+'9'
        if i=="ZER":
            n=n+'0'
    return n
def totriple(ans):
    strnum=str(ans)
    n=str()
    for i in strnum:
        if i=="1":
            n=n+'ONE'
        if i=="2":
            n=n+"TWO"
        if i=="3":
            n=n+"THR"
        if i=="4":
            n=n+"FOU"
        if i=='5':
            n=n+"FIV"
        if i=='6':
            n=n+"SIX"
        if i=="7":
            n=n+"SEV"
        if i=="8":
            n=n+"EIG"
        if i=="9":
            n=n+"NIN"
        if i=="0":
            n=n+"ZER"
    return n
s=str(input())
j=s.find("+")
s1=s[:j]
s2=s[j+1:]
f1=transfer(s1)
f2=transfer(s2)
ans=int(f1)+int(f2)
print(totriple(ans))

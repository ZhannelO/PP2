import collections
from collections import OrderedDict
n = int(input())
list = []
for i in range(n):
    s=dict()
    string=str(input())
    word=string.split() 
    s[word[0]]=int(word[1])
    list.append(s)
counter = collections.Counter()
for d in list:
    counter.update(d)
res = dict(counter)
num=[]
for x in res:
    num.append(res[x])
max=int(num[0])
for i in range(len(num)):
    if num[i]>max:
        max=num[i]
ans=[]
for j in res:
    if res[j]<max:
        tenge=max-res[j]
        wer=str(j)+" " +"has to receive"+" "+str(tenge)+" "+"tenge"
        ans.append(wer)
    if res[j]==max:
        wer=str(j)+" "+"is lucky!"
        ans.append(wer)
for i in sorted(ans):
    print(i)
import string
s=str(input())
k = s.translate(str.maketrans('', '', string.punctuation))
word=k.split()
u=set()
for i in word:
    u.add(i)
pop=[]
for i in u:
    pop.append(i)
upper=[]
lower=[]
for x in pop:
    if 'A'<=x[0] and  x[0]<= 'Z':
        upper.append(x)
    if 'a'<=x[0] and x[0] <='z':
        lower.append(x)
print(len(u))
for i in sorted(upper):
    print(i)
for j in sorted(lower):
    print(j)
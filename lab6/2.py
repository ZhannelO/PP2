#Write a Python program with builtin function that accepts
# a string and calculate the number of upper case letters and lower case letters
def upper(string):
    cnt=0
    for i in string:
        if 65<=int(ord(i)) and int(ord(i))<=90:
            cnt+=1
    print("Upper case letters"+":"+str(cnt))
def lower(string):
    count=0
    for i in string:
        if 97<=int(ord(i)) and int(ord(i))<= 122:
            count+=1
    print("Lower case letters"+":"+str(count))
s=str(input())
upper(s)
lower(s)


#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
txt="abb Kabinskoe doll joke people abbbbbbbbbb abc  west king Haley ACM python school KBTU university FIT Hat"
textlookfor=r"ab*" 
x=re.findall(textlookfor, txt)
print(x)
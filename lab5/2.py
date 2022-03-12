#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
txt="abb Kabinskoe doll joke people abbb abbc  west king Haley ACM python kaaaabbbbbbek school KBTU university FIT Hat"
textlookfor="ab{2,3}" 
x=re.findall(textlookfor, txt)
print(x)
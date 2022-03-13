#Write a Python program to split a string at uppercase letters.
import re
txt="SnakeCaseStringConverstToCamelCase"
res=re.findall("[A-Z][^A-Z]*",txt)
print(res)
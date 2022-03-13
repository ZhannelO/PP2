#Write a Python program to insert spaces between words starting with capital letters.
import re
txt="SnakeCaseStringConverstToCamelCase"
res=re.sub(r"(\w)([A-Z])",r"\1 \2",txt)
print(res)

#Write a Python program to convert a given camel case string to snake case.
import re
REG="(.+?)([A-Z])"
def snake(camel):
    return camel.group(1).lower()+"_"+camel.group(2).lower()
txt="CamelStringToSnakeString"
res=re.sub(REG,snake,txt,0)
print(res)



#Write a python program to convert snake case string to camel case string.
import re
def camel(snake):
    return snake.group(1)+snake.group(2).upper()
REG = r"(.*?)_([a-zA-Z])"
txt="snake_case_string_converst_to_camel_case"
res=re.sub(REG,camel,txt,0)
print(res)

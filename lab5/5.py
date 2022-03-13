#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
txt="PRIVET, 2003 .2010.04.02 qazaq  VS_CODE,seGment,kBtU UnIvErSiTy;python ^zhannel@gmail.com Phone%number "
x=re.sub("[ .,]", ":" , txt)
print(x)
#WWrite a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
txt="PRIVET 2003 2010 04 qazaq VS_CODE seGment kBtU UnIvErSiTy python zhannel@gmail.com Phone number "
textlookfor="[A-Z]+[a-z]" 
x=re.findall(textlookfor, txt)
print(x)
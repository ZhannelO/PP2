#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
txt="PRIVET, 2003 .2010.04.02 qa43543656_adpsdsorb VS_CODE,seGment,kBtU a2003b UnIvErSiTy;python ^zhannel@gmail.com Phone%number aabb "
textlookfor="a.*b$"
x=re.findall(textlookfor,txt)
print(x)
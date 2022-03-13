#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
txt="TELE_PHON p_y_t_h_o_n guitar 32144 3_5_6_8 co_de VS_CODE George 1992 03 04 google@gmail.com problem_3 PP_2 git_hub "
textlookfor="[a-z]+_[a-z]" 
x=re.findall(textlookfor, txt)
print(x)
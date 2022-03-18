#Write a Python program with builtin function that checks whether a passed string is palindrome or not
def is_Palindrome(string):
	left = 0
	right = len(string) - 1
	
	while right >= left:
		if not string[left] == string[right]:
			return False
		left += 1
		right -= 1
	return True
s=str(input())
print(is_Palindrome(s)) 



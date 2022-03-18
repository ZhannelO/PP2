#Write a Python program to write a list to a file
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as file:
        for c in color:
                file.write("%s\n" % c)

ans = open('abc.txt')
print(ans.read())
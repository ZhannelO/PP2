#Write a Python program to count the number of lines in a text file.
def lenght(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",lenght("test.txt"))

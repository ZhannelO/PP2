class My_class:
    def getString( self ):  #to get a string from console input printString
        self.printString(input())

    def printString(self,message): #to print the string in upper case.
        print(message.upper())

s=My_class()
s.getString()


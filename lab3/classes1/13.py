def Guess_the_num():
    x=15
    name=input("Hello! What is your name? \n")
    print("Well"+","+str(name)+","+"I am thinking of a number between 1 and 20.")
    cnt=0
    user_guess=input("Take a guess.\n")
    while(user_guess!=x):
        cnt=cnt+1
        if int(user_guess)<x:
            print("Your guess is too low.")
            cnt=cnt+1
            user_guess=input("Take a guess\n")
        if int(user_guess)>x:
            print("Your guess is too big!")
            cnt=cnt+1
            user_guess=input("Take a guess\n")
        if int(user_guess)==x:
            break
    print("Good job"+","+str(name)+","+"You guessed my number in"+" "+str(cnt)+" "+"guesses!")
Guess_the_num()


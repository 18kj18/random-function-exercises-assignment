import random as random

def q52():
    '''Display random int between 1 and 100, inclusive'''
    return random.randint(1, 100)

def q53():
    '''Display random fruit from a list of 5'''
    return random.choice(["Apple", "Orange", "Grape", "Pineapple", "Fruit number 5"])

def q54():
    '''Guess if computer picked heads or tails'''
    compChoice = random.randint(1,2)
    userChoice = int(input("Guess which the computer picked\nHeads:1\tTails:2\n--> "))
    if userChoice == compChoice:
        win = True
    else:
        win = False
        
    print("Well Done! The computer chose Heads!" if compChoice == 1 else "Bad Luck.The computer chose Tails!")
    return win

def q55():
    '''Guess a random number, hot or cold style, 2 guesses'''
    randomNumber = random.randint(1,5)
    
    userGuess = int(input("The computer has picked a number from 1 to 5, guess what it chose\n--> "))
    
    if userGuess == randomNumber:
        print("You Win!")
        return True
    elif userGuess > randomNumber:
        userGuess = int(input("The number is lower than that!\nGuess again\n -->"))
        if userGuess == randomNumber:
            print("You Win!")
            return True
        else:
            print("You Lose :(")
            return False
        
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
            print("You Lose :(\nThe number was", randomNumber)
            return False
        
    else:
        userGuess = int(input("The number is greater than that!\nGuess again\n -->"))
        if userGuess == randomNumber:
            print("You Win!")
            return True
        else:
            print("You Lose :(\nThe number was", randomNumber)
            return False
        
def q56():
    '''Guess a random nuber between 1-10, unlimited guesses'''
    randomNumber = random.randint(1,10)
    userNumber = int(input("The computer has picked a number from 1 to 10, you have unlimited guesses\n--> "))
    
    while userNumber != randomNumber:
        if userNumber > randomNumber:
            print("The number is lower than that!")
        else:
            print("The number is higher than that!")
        userNumber = int(input("Try again\n--> "))
    
    print("Congratulations!")
    return True

def q58():
    '''maths quiz, addition, score out of 5'''
    
    
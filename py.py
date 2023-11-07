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
    score = 0
    for i in range(0,5):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        if int(input(f"What is the sum of the numbers {num1} and {num2}\n--> ")) == num1 + num2:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print("Your total score out of 5 is", score)
            
def q59():
    colorlist = ["red", "orange", "yellow", "green", "blue"]
    color = random.choice(colorlist)
    
    match color:
        case "red":
            hint = "something something RED something"
        case "orange":
            hint = "something somehting BLUE something"
        case "yellow":
            hint = "something YELLOW somehing something"
        case "green":
            hint = "GREEN something something"
        case "blue":
            hint = "BLUE somehintg"
    
    print("Red, Orange, Yellow, Green, Blue")
    correct = 0
    while correct == 0:
        inp = input("Pick one of these 5 colors:\n--> ").lower()
        
        if inp == color:
            print("Correct!")
            correct = 1
        else:
            print("Hint -> ", hint)
            
        
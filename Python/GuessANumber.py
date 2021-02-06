number = 13

guess = input("Enter an number: ")
guessedNumber = int(guess)

while True:
    if guessedNumber == number:
        print("Congrats! You got it!")
        break
    elif guessedNumber > number:
        print("A bit lower. Try again")
    else:
        print("A bit higher. Try again.")
        
    guess = input("Enter an number: ")
    guessedNumber = int(guess)


    
    
    
    

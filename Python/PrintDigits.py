# Read a number from the keyboard
# Print each digits (starting with unit place) on individual lines
# For eg for 345, print 5 and then 4 and then 3 on 3 lines
while True:
    number = input("Enter an integer: ")
    enteredNumber = int(number)

    while enteredNumber > 0:
        digit = enteredNumber % 10
        print(digit)
        
        enteredNumber = enteredNumber // 10


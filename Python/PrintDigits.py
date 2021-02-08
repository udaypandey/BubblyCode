# Read a number from the keyboard
# Print each digits (starting with unit place) on individual lines
# For eg for 345, print 5 and then 4 and then 3 on 3 lines

number = input("Enter an integer: ")
enteredNumber = int(number)

numberFlip = enteredNumber % 10
numberFlip2 = (enteredNumber // 100) % 10
numberFlip3  = (enteredNumber // 100) 


print(numberFlip * 100 + numberFlip3 * 10 + numberFlip2 )


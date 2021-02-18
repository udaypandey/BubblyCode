# Read a number from the keyboard
# Print reverse number
# For eg for 1234567, 7654321
num = int(input("Enter a number: "))  
sum = 0

while num > 0:
    remain = num % 10
    sum = sum * 10 + remain
    
    num = num // 10
    
print(sum)
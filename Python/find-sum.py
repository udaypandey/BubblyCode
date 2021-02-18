# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
# for eg for 4, it will add 1, 2, 3, 4
def bubbles_sum(num):
    sum = 0

    for a in range(1, num + 1): 
        sum = sum + a
    
    return sum

def uday_sum(num):
    sum = 0
    
    while num > 0:
        sum += num
        num -= 1
        
    return sum
    
while True:
    num = int(input("Enter number: "))
    print(uday_sum(num))

    
     
    
    

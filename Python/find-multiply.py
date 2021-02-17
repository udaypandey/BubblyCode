# Write a program that asks the user for a number n and prints the multiplication of the numbers 1 to n
# for eg for 4, it will multiply 1, 2, 3, 4

def multiAll(n) :
    multi = 1
    while n > 0:
        if n % 2 == 1:
            multi = multi * n
        n = n - 1
        
    return multi


print(multiAll(9))
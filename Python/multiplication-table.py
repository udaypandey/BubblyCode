# Write a program that prints a multiplication table for numbers up to 12.

def printTable() :
    num = 1
    while num <= 12:
        end = 12
        start = 1
        
        while start <= end:
            print(f"{num} x {start} = {num *  start}")
            start = start + 1
        num = num + 1
            
            
    
    
printTable()
    
# if list, print all even numbers

def print_even(list):
    index = 0
    
    while index < len(list):
        if list[index] % 2 == 0:
            print(list[index])
            
        index = index + 1


# list = [1, 2, 3, 4, 5, 6]
# print_even(list)

list = [8, 46, 67, 98, 101]
print_even(list)

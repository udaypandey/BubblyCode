# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
num = int(input("Enter number: "))
def bubbles_sum(num):
    sum = 0

    for a in range(1, num + 1): 
        sum = sum + a
        if (a % 3 == 0 or a % 5 == 0) :
            sum = sum + a
            print(sum)
    
    





numbers = [11, 12, 13, 14, 15]
# # for number in numbers:
# #     print(number)
#     
# numbersCount = len(numbers)
# # print(numbersCount)
# idx = 0
# while idx < numbersCount:
#     print(numbers[idx])
#     idx += 1
# squareNumbers = []
# 
# for number in numbers:
#     squareNumbers.append(number**2)
# 
# print(squareNumbers)
numbersCount = len(numbers)
idx = 0
totalSum = 0
while idx < numbersCount:
    totalSum += numbers[idx]
    idx += 1 

print(totalSum)


sum = 0
for number in numbers:
    sum += number
    
print(sum)
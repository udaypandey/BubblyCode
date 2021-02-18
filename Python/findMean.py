def aMean(list):
    sum = 0
    
    for item in list:
        sum += item
    
    return sum / len(list)

list2 = [2, 65, 23]
print(aMean(list2))

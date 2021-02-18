def aRange(list):
    max = list[0]
    min = list[0]
    
    for item in list:
        if item > max:
            max = item
        if item < min:
            min = item
    
    return max - min

list2 = [1, 65, 23, 0, 10, 2, 3, 89, 8, 7, 34, -45]
print(aRange(list2))


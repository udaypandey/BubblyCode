def multList(list):
    mult = 1
    
    for item in list:
        mult *= item
    
    return mult

list2 = [2, 3, 4, 5]
print(multList(list2))

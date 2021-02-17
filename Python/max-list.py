
def aMax (list):
    if len(list) == 0:
        return None
    max = list[0]
    for item in list:
        if item > max:
            max = item
    return max
            
    
    
    
def aMin (list):
    if len(list) == 0:
        return None
    
    min = list[0]
    for item in list:
        if item < min:
            min = item
    return min
    

list = [1, 65, 23, 0, 10, 2, 3, 89, 8, 7, 34, -45]
list2 = [-1, -65, 0, -23, -45]

print(aMax(list))
print(aMin(list))
print(aMax(list2))
print(aMin(list2))

print(aMax([]))
print(aMin([]))


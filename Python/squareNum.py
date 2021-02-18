def squareNum(list):
#     for item in list:
#         item = item * item
    l = len(list)
    i = 0
    while i < l:
        list[i] *= list[i]
        i += 1

# l = len(a)
# i = 0
# while i < l:
#     print(f"{i+1}: {a[i]}")
#     i += 1
list2 = [2, 3, 4]
print(list2)

squareNum(list2)
print(list2)
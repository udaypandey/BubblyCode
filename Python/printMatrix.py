def printMatrixWhile(matrix):
    i = 0
    while i < len(matrix) :
        j = 0
        row = matrix[i]
        while j < len(row):
            print(row[j])
            j += 1
        i += 1

def printMatrixFor(matrix):
    for row in matrix:
        for col in row:
            print(col)
    
m = [[1, 2, 3], [4, 5,6, 7, 8, 9], [17,18]]
# printMatrixWhile(m)

printMatrixFor(m)

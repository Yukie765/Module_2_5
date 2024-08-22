def get_matrix (n,m,value):
    matrix = []
    for i in range(0,n):
        new_line = []
        for j in range(0,m):
            new_line.append(value)
        matrix.append(new_line)
    return matrix


print(get_matrix(2,2,10))
print(get_matrix(3,5,42))
print(get_matrix(4,2,13))
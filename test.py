def stage1():
    mat = []
    for row in range(12):
        n_row = []
        for col in range(1, 13):
            n_row.append(12 *row +col)
        mat.append(n_row)
    return mat




def stage2(mat):
    new_mat = []
    for row in range(len(mat)):
        n_row = []
        for col in range(len(mat[row])):
            if col % 2 == 0:
                n_row.append(mat[row][col]+col)
            else:
                 n_row.append(mat[row][col])
        new_mat.append(n_row)
    return new_mat



def sum_of_digits(number):
    sum = 0
    str_number = str(number)
    for i in range(len(str_number)):
        sum += int(str_number[i])
    return int(sum)
print(sum_of_digits(143))

def stage3(mat):
    new_mat = []
    for i in range(len(mat)):
        n_row = []
        n= len(mat)
        for j in range(len(mat[i])):
            n_row.append(sum_of_digits(mat[i][j]))
        new_mat.append(n_row)

    return new_mat
print(stage3(stage1()))

def stage4(mat):
    new_mat = []
    for i in range(len(mat)):
        n_row = []
        for j in range(len(mat[i])):
            if i % 2 == 1:
                n_row.append(mat[i][j] + (i*2))
            else:
                n_row.append(mat[i][j])
        new_mat.append(n_row)
    return new_mat
print(stage4(stage1()))

def mul_and_add(row_number, column_number, cell_value):
    return (row_number * column_number + cell_value)
print(mul_and_add(2,1,5))

def stage5(mat):
    n_mat = []
    for row in range(len(mat)):
        n_row = []
        for col in range(len(mat[row])):
            n_row.append(mul_and_add(row,col,mat[row][col]))
        n_mat.append(n_row)
    return n_mat
print(stage5(stage1()))

def stage6(mat, col):
    number = mat[-1][col]
    for row in range(len(mat)):
        mat[row-1][col] = mat[row][col]
    mat[-2][col] = number
    return mat
mat=stage6(stage1(),0)
for i in mat:
    print(i)



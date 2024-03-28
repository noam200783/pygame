# print( [[ ]*nun]*6)

def make_square_mat(num):
    mat = []
    for i in range(num):
        col = []
        for j in range(num):
            col.append(0)
        mat.append(col)
    return mat
print(make_square_mat(4))

def fix_tv(tv):
    not_working = []
    for i in range(len(tv)):
        for j in range(len(tv[i])):
            if tv[i][j] == "problem":
                not_working.append((i, j))
    return not_working
print(fix_tv([["problem","work","problem","work", "work"],
              ["problem", "work", "work", "work","problem"]]))

def avg(mat):
    total = 0
    total_num = 0
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            total += mat[row][col]
            total_num += 1
    print(total/total_num)
avg([[10, 2, 3], [4, 5, 6], [7, 8, 9]])

def hzi(list1):
    list1.sort
    return (list1[int(len(list1)/2)])

print(hzi([1,5,8,9,7,3,4,2,15,12]))

def noam(list2, num):
    num = num % len(list2)
    print(list2[num::], list2[:num:])
    return list2[num::] + list2[:num:]
print(noam([1,2,3,4,5,6,1,8,7,9,9,9], 4))

def gfd(string):
    d = ""
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            d += i
    return d
print(gfd("albus dumbeldor"))

def product():
    my_dict = dict()
    name_product = input("enter a name product")
    if name_product != "done":
        inventory = input("enter yes or no")
    while name_product != "done":
        my_dict[name_product] = inventory
        name_product = input("enter a name product")
        if name_product == "done":
            break
        inventory = input("enter yes or no")
    keys = my_dict.keys()
    for i in keys:
        if my_dict[i] == "no":
            print(f"The product {i} is not in stock")
        else:
            print(f"The product {i} is in stock.")

product()


num = 123456789
number = str(num)
sum = 0
for i in range(len(number)):
    print(number[i])
    sum += int(number[i])
print(int(sum))



def foo(mat):
    even = True
    for row in mat:
        for col in range(len(row)):
            if (col%2 ==0) == even:
                print(row[col])
        even = not even

foo(make_square_mat(10))
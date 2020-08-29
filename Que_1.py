row_num = int(input("Enter number of rows: "))
col_num = int(input("Enter number of columns: "))
array = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        array[row][col]= row*col

print(array)
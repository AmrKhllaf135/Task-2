str1 ="AMR"
print_A = [[" " for i in range(5)] for j in range(6)]
print_M = [[" " for i in range(5)] for j in range(6)]
print_R = [[" " for i in range(5)] for j in range(6)]
#code for A:
for row in range(6):
    for col in range(5):
        if ((col == 0 or col == 4) and row != 0) or row ==2 or (row == 0 and col != 0 and col != 4):
            print_A[row][col] = "*"

#code for M:
for row in range(6):
    for col in range(5):
        if col == 0 or col ==4 or (col == row and row <3) or (row+col == 4 and row <3):
            print_M[row][col] = "*"
#code for R:
for row in range(6):
    for col in range(5):
        if col == 0 or ( col == 4 and ( row !=3 and row != 0)) or (row == 0 or row ==3 and (col > 0 and col < 4))  :
            print_R[row][col] = "*"
for i in range(6):
    for j in range(5):
        print(print_A[i][j], end = " ")
    print(end = "   ")
    for j in range(5):
        print(print_M[i][j], end = " ")
    print(end = "   ")
    for j in range(5):
        print(print_R[i][j], end = " ")
    print(end = "   ")
    print( )


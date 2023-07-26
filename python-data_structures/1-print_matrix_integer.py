#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    #!/usr/bin/env python3
    for row in matrix:
        if not row:
            print()  
        else:
            for i in range(len(row)):
                if i == len(row) - 1:
                    print("{:d}".format(row[i]))
                else:
                    print("{:d}".format(row[i]), end=" ")

tests = input("Enter number of tests\n")

for i in range(int(tests)):
    print(i)

    columns = input("Enter number of columns\n")
    Matrix = [[0 for x in range(columns)] for y in range(columns)]
    Matrix[0][0] = 1

#
# Mario Jimenez
#
# https://www.hackerrank.com/challenges/beautiful-binary-string

# Get in binary string
# for each 010, change the last 0 to a 1.
length = input("Enter Length\n")
binaryString = input("Enter binary string\n")
count = 0
for x in range(2, int(length)):
    if (binaryString[x - 2] == '0' and
        binaryString[x - 1] == '1' and
            binaryString[x] == '0'):
        binaryString = binaryString[:x] + '1' + binaryString[x + 1:]
        count += 1
print(count)

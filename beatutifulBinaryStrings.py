#
# Mario Jimenez
#


# Get in binary string
# for each 010, change the last 0 to a 1.
binaryString = input("Enter binary string\n")
length = len(binaryString)
count = 0
for x in range(2, length):
    if(binaryString[x-2] == '0' and binaryString[x-1] == '1' and binaryString[x] == '0'):
        binaryString[:2] + '1' + binaryString[2:]
        count += 1
print(count)

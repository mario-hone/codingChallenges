#
# Author: Mario Jimenez
# Description: Factorial
#

def Factorial(num):

    count = num

    while count > 1:

        #print count
        #print "num: %s" %num

        num *= (count - 1)
        count -= 1

    return num

#print Factorial(2)
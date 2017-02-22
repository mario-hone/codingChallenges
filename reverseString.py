#
# Have the function FirstReverse(str) take the str parameter being passed and
# return the string in reversed order.
#
# For example: if the input string is "Hello World and Coders"
# then your program should return the string sredoC dna dlroW olleH.

def FirstReverse(str):

    # In python you can treat the string as an array by adding [] after it and
    # the colons inside represent str[start:stop:step] where if step is a negative number
    # it'll loop through the string backwards
    return str[::-1]

# keep this function call here
print FirstReverse("Hello World!")
print FirstReverse("Texas Tech University Keyboardless Mac Room")

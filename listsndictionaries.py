# This is a program to practice using lists and dictionaries in Python

# There are 4 types of collections:
# List - ordered (indexed) and changeable. Allows duplicate members. Use square brackets []
# Tuple - ordered and unchangeable. Allows duplicate members. Use parenthesis ()
# Set -  unordered and unindexed. No duplicate members. Use curly brackets {}
# Dictionary - unordered, changeable and indexed. No duplicate members. Use curly brackets and colon{key:value}

# List - ordered and changeable. Allows duplicate members. Use square brackets []
# list elements do not all have to be the same type
mylist = [1, "red", "true", 3.14159]
print(mylist)
# list indices start at 0
print('The second element in the list is ' + mylist[1])
print(mylist[0] + mylist[3])
# list elements can be changed
mylist[2] = 'false'
print(mylist)

# Tuple - ordered and unchangeable. Allows duplicate members. Use parenthesis ()
# tuple elements do not all have to be the same type
mytuple = ("mom", "dad", 2.5)
print(mytuple)
print('The second element in the tuple is ' + mytuple[1])
# tuple elements cannot be changed - trying to change them results in a TypeError
try:
        mytuple[1] = "sister"
        print(mytuple)
except TypeError:
        print('Trying to change a tuple element results in a TypeError')

print('The second element in the tuple is still ' + mytuple[1])


# Set -  unordered and unindexed. No duplicate members. Use curly brackets {}
myset = {'apple', 'orange', 'banana', 'apricot'}
print(myset)


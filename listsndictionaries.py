# This is a program to practice using lists and dictionaries in Python

# There are 4 types of collections:
# List - ordered (indexed) and changeable. Allows duplicate members. Use square brackets []
# Tuple - ordered and unchangeable. Allows duplicate members. Use parenthesis ()
# Set -  unordered and unindexed. No duplicate members. Use curly brackets {}
# Dictionary - unordered, changeable and indexed. No duplicate members. Use curly brackets and colon{key:value}

# List - ordered and changeable. Allows duplicate members. Use square brackets []
# list elements do not all have to be the same type
print('\n---------------LIST EXAMPLE---------------\n')
mylist = [1, "red", "true", 3.14159]
print('original list:')
print(mylist)
# list indices start at 0
print('The second element in the list is ' + mylist[1])
print(mylist[0] + mylist[3])
# list elements can be changed
mylist[2] = 'false'
print(mylist)

# Tuple - ordered and unchangeable. Allows duplicate members. Use parenthesis ()
# tuple elements do not all have to be the same type
print('\n---------------TUPLE EXAMPLE---------------\n')
mytuple = ("mom", "dad", 2.5)
mytuple2 = ("Amy", "Gabrielle", "Karen", "Santa Claus")
print(mytuple)
print('The second element in this tuple is ' + mytuple[1])
print(mytuple2)
print('The third element in the second tuple is ' + mytuple2[3])
# tuple elements cannot be changed - trying to change them results in a TypeError
try:
        print('Try to change the second element from dad to sister: \n')
        mytuple[1] = "sister"
        print(mytuple)
except TypeError:
        print('Trying to change a tuple element results in a TypeError')

print('The second element in the tuple is still ' + mytuple[1])


# Set -  unordered and unindexed. No duplicate members. Use curly brackets {}
print('\n---------------SET EXAMPLE---------------\n')
myset = {'apple', 'orange', 'banana', 'apricot'}
print(myset)
myset.add('cantalope')
print(myset)


# Dictionary - unordered, changeable and indexed. No duplicate members. Use curly brackets and colon{key:value}
print('\n---------------DICTIONARY EXAMPLE---------------\n')
mydictionary = {"apple": "red", "orange": "orange", "banana": "yellow", "grape": "green"}
print(mydictionary)
print(mydictionary["apple"])
for fruit in mydictionary:
        print("The " + fruit + " is " + mydictionary[fruit])
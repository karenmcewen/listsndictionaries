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

# Dictionary - unordered, changeable and indexed by key:value pairs.
# #No duplicate members allowed. Use curly brackets and colon{key:value}
print('\n---------------DICTIONARY EXAMPLE---------------\n')
mydictionary = {"apple": "red", "orange": "orange", "banana": "yellow", "grape": "green"}
print(mydictionary)
print(mydictionary["apple"])
for fruit in mydictionary:
    print("The " + fruit + " is " + mydictionary[fruit])

print('original dictionary')
print(mydictionary)

# Changing lists
mybooks = ["Python Crash Course", "Big Data", "Murder Mystery Mayhem"]
print(mybooks)
# append adds to the end of the list
mybooks.append("Sci-Fi Fav")
print(mybooks)
# insert adds at the given position
mybooks.insert(2, "Cook with Book")
print(mybooks)
# sort will sort alphanumerically by default
mybooks.sort()
print("My books in alphabetical order: ", mybooks)
# pop pops up the final item in the list but keeps it in limbo so you can continue to use it a bit
last_book = mybooks.pop()
print("the last book in my collection is: ", last_book)
print("I gave it up seeking the Holy Grail.  My current books are: ", mybooks)

mybooks.append("Cook with Book")
print(mybooks)
mybooks.sort()
print("My books in alphabetical order: ", mybooks)
print("Oops! Looks like I got a double. I will remove it!")
extra_book = "Cook with Book"
mybooks.remove(extra_book)
print("My books in alphabetical order: ", mybooks)
# len tells how many are in the list
print("I have ", len(mybooks), " books!")

# looping with lists
for books in mybooks:
    print(books)

# f before a string will insert its value
# .title() changes list item to title case (first letter is capitalized)
for books in mybooks:
    print(f"{books.title()} is one of my favorite books!")

# while loop
i = 0
while i<len(mybooks):
    print(mybooks[i])
    i = i + 1
print("done with books!")

# making a list of numbers
# range(x,y,z) starts with x, ends with y-1, z is interval between numbers
for value in range(1,20,3):
    print(value)

# creating a new list of squares of numbers
# starting with an empty list
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    print("square of", value, "is", square, "and cube is", value**3)
print(squares)

# you can shorten the for statement by combining lines
cubes = []
for value in range(1,11):
    cubes.append(value**3)

print(cubes)

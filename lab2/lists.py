#exercise 1

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#exercise 2

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#exercise 3

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#exercise 4

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#exercise 5

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#exercise 6

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#exercise 7

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2 : 5])

#exercise 8

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#examples

#Create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Loop trough a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Add an item to the end of a list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Add an item at a specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Remove an item at a specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#exercise 1

fruits = ("apple", "banana", "cherry")
print(fruits[0])

#exercise 2 

fruits = ("apple", "banana", "cherry")
print(len(fruits))

#exercise 3

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#exercise 4

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2 : 5])

#examples

#Loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Check if a tuple item exists 
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Get the length of a tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Delete a tuple 
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Using the tuple() coonstructor to create a tuple
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
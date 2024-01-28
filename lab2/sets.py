#exercise 1

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#exercise 2
  
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#exercise 3

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#exercise 4

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#exercise 5

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#examples

#Add multiple items to a set
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

#Get the length of a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Remove an item in a set by using the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Remove the last item in a set by using the pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal

#Using the set() constructor to create a set
thisset = set(("apple", "banana", "cherry"))
print(thisset)
#the set list is unordered, so the result will display the items in a random order.
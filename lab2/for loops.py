#exercise 1 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#exercise 2
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#exercise 3 

for x in range(6):
    print(x)

#exercise 4
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

#examples

#Else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
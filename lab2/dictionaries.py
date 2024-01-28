#exercise 1

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#exercise 2 

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#exercise 3

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#exercise 4

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#exercise 5 

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#examples

#Print all key names in a dictionary, one by one
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

#Using the values() function to return values of a dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

#Loop through both keys an values, by using the items() function
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

#Empty a dictionary
  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Using the dict() constructor to create a dictionary
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
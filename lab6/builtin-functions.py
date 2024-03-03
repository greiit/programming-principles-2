#1
list1 = [1, 2, 3, 4, 5]
print(eval("*".join(str(x) for x in list1)))

#2
string = input("enter the string: ")
lc = 0
uc = 0
for c in string:
    if ord(c) < 91 and ord(c) > 59:
        lc = lc + 1
    elif ord(c) > 96 and ord(c) < 123:
        uc = uc + 1
print(f"count of uppercase letters is {uc}, and lowercase letter is {lc}")

#3
string = input("enter any word of your that you may suggest as a pallindrome: ")
def revstr(s):
    return "".join(c for c in reversed(string))
while(string != revstr(string)):
    string = input("try one more time: ")
else:print("happy for you, its a pallindrome here!")

#4
from time import sleep
number, milisec = [int (z) for z in input("enter number and time: ").split(" ")]
sleep(milisec/1000)
print(pow(number, 0.5))


#5
tuple1 = ("nsdkm", True, 654)
print(all(tuple1))

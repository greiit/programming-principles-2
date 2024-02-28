#1
import re
x = str(input())
check = re.search("ab*", x)
print(check)

#2
bb = str(input())
bbb = re.search("a[b]{2,3}", bb)
print(bbb)

#3
az = str(input())
azz = re.findall("[a-z]+_[a-z]+", az)
print(azz)

#4
uppercase = str(input())
upplow = re.findall("[A-Z][a-z]+", uppercase)
print(upplow)

#5
a = str(input())
ab = re.search(r"[a].*[b]$", a)
print(ab)

#6
txt = str(input())
subtxt = re.sub("[ ,.]", ":", txt)
print(subtxt)

#7
def snake_to_camel_case(snake_str):
    components = snake_str.split('_')
    if components:
        camel_case_str = components[0] + ''.join(x.title() for x in components[1:])
    else:
        camel_case_str = ''
    return camel_case_str

string = "snack_case"
camel_case = snake_to_camel_case(string)
print(camel_case)

#8
def split_at_uppercase(s):
    return re.findall('[A-Z][^A-Z]*', s)
print(split_at_uppercase("plpPPplpLLLL"))

#9
def insert_spaces(s):
    return re.sub(r'(?<=[a-zA-Z])(?=[A-Z])', ' ', s)
print(insert_spaces("AnitaMaxWynn"))

#10
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
print(camel_to_snake("aNewSeasonIsComing"))
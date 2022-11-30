a = "tjis is astring. this is a string."
b = "123"
print(a.count("t"))
print(a.count("this"))
print("count",b.count("1"))
b = "java is simple"

c = "."
l1 = ["www","google","co","in"]
l2 = "Yahoo"
print(c.join(l1))
print(c.join(l2))

c = "hello"
d = "ABC"
print(c.isupper())
print(d.isupper())
print(c.islower())
print(d.islower())

c = "hello"
d = "ABC"
print("Is upper", c.isupper())
print("Is upper", d.isupper())
print(c.islower())
print(d.islower())
print("Is alphabets", c.isalpha())
d = "ABC23ab"
print(d.isalpha())
print(d.isalnum())

d = "ABC23ab@q12"
print(d.isalnum())
d = "123"
print("is Digit",d.isdigit())
d = "  "
print("is space",d.isspace())
print("is identifier",d.isidentifier())
d = "123q"
print("is Digit",d.isdigit())
d = " h "
print("is space",d.isspace())

a = "Hello World"
print(a.istitle())

a = "Hello\tworld"
print(a)

z = "It's very humid outside"
print(z)

str1 = input("Str1: ")
str2 = input("Str2: ")
l1 = len(str1)
l2 = len(str2)
if(l1==l2):
    print("Strings are samne length")
elif(l1>l2):
    print(str2+str1+str2)
else:
    print(str1+str2+str1)

a = "Hello Python"
print(a.find('p'))

import string
print(string.punctuation)
print(string.digits)
print(string.hexdigits)
print(string.ascii_letters)
print(string.printable)
print(string.capwords("hello world"))
print(string.octdigits)

import string
punctuations = string.punctuation
result = ""
str = "list-[]\n tuple-()\n Dictionary-="
for i in str:
    if i not in punctuations:
        result=result+i
print("Set of puctuations in string.puctuation is:",punctuations)
print("String after removing all Punctuation's is:",result)
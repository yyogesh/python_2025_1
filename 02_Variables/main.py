userName = "user_name" # camelCase
user_name = "user_name" # snake_case # preferred in Python
user_name = "user_name" # kebab-case (not valid in Python)
UserName = "user_name" # PascalCase

a = 10

b = "abc"

c = True

a, b, c = 10, "abc", True

a = b = c = 10

print(type(a), type(b), type(c))

PI = 3.14 # constant by convention

# python main.py

"""Hello this 
multiline comment"""

print(a.__sizeof__()) # size in bytes

a = 10

print(a, a.__sizeof__())

a = 12.58
print(a, a.__sizeof__())

b = 12456789012345678901234567890
print(b, b.__sizeof__(), type(b))

a = True
print(a, type(a), int(a))

x = 25 + 3j
print(x, type(x))

print(x.real, x.imag, x.conjugate(), x.real)

a = 20

print(bin(a), oct(a), hex(a))

# int() # float() # complex() # bool() # str() # list() 
# # tuple() # set() # dict() # frozenset() # bytes() # bytearray() # memoryview() # range() # None


i = "15"
x = float(i)
print(x, type(x))


g = int(input("Enter a number: "))
print(g, type(g), id(g))
# Identity operators are used to compare the memory locations of two objects.

# Operator	Description	Example
# is	True if both variables point to the same object	a is b
# is not	True if both variables point to different objects	a is not b


a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]

print("a is b:", a is b, id(a), id(b))
print("c is d:", c is d)
print("c is not d:", c is not d) 
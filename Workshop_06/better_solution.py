def is_odd(x):
    if x % 2:
        return True
    else:
        return False


def is_all_even(*numbers):
    for i in numbers:
        if is_odd(i):
            return False
    return True


def greatest_number(*numbers):
    greatest = numbers[0]
    for i in numbers:
        if i > greatest:
            greatest = i
    return greatest


print("---Aspect 1---")
x = int(input("input integer X: "))
if is_odd(x):
    print("X is odd.")
else:
    print("X is even.")
print()

print("---Aspect 2---")
y = int(input("input integer Y: "))
print("The greater number is %d." % greatest_number(x, y))
print()

print("---Aspect 3---")
if is_all_even(x, y):
    print("There is no odd number.")
else:
    temp = greatest_number(x, y)
    if is_odd(temp):
        print("The greater odd number is %d." % temp)
    else:
        print("No output this time.")
print()

print("---Aspect 4---")
z = int(input("input integer Z: "))
if is_all_even(x, y, z):
    print("There is no odd number.")
else:
    temp = greatest_number(x, y, z)
    if is_odd(temp):
        print("The greater odd number is %d." % temp)
    else:
        print("No output this time.")

print("---Aspect 1---")
x = int(input("input integer X: "))
if x % 2:
    print("X is odd.")
else:
    print("X is even.")
print()

print("---Aspect 2---")
y = int(input("input integer Y: "))
print("Y = %d" % y)
print()

print("---Aspect 3---")
if x % 2 == 0 and y % 2 == 0:
    print("There is no odd number.")
elif x % 2 and x > y:
    print("X(=%d) is odd and bigger than Y(=%d)" % (x, y))
elif y % 2 and y > x:
    print("Y(=%d) is odd and bigger than X(=%d)" % (y, x))
else:
    print("Something else.")
print()

print("---Aspect 4---")
z = int(input("input integer Z: "))
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print("There is no odd number.")
elif x > y and x > z:
    if x % 2:
        print("X(=%d) is odd and the biggest number." % x)
elif y > x and y > z:
    if y % 2:
        print("Y(=%d) is odd and the biggest number." % y)
elif z > x and z > y:
    if z % 2:
        print("Z(=%d) is odd and the biggest number." % z)
else:
    print("Something else.")

a = [""] * 3
print(a)
for i in range(3):
    a[i] = input("a[%d]: " % i)
a.sort()
print(a)

a = []
print(a)
i = 0
while i < 3:
    a.append(input("a[%d]: " % i))
    i += 1
print(sorted(a))
"""
sorted関数は、指定したリストaを複製してソートした新しいリストを返しますので、
もとのリストaはソートされません。
"""

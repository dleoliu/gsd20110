# あらかじめ、3つの空文字列を要素とするリストを定義。a[2]まで添字アクセスできて書換もできる。
a = [""] * 3
print(a)

# ここに3行、inputを使ってリストの要素を変更しましょう
a[0] = input("a[0]: ")
a[1] = input("a[1]: ")
a[2] = input("a[2]: ")

# 続いて、リストをソートして、表示してみましょう。
a.sort()
print(a)

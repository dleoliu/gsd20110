# あらかじめ、要素を持たないリストを定義。a[0]すら存在しない。a=[]
a = []
print(a)

# ここに3行、inputを使ってリストの要素をappendしましょう
a.append(input("a[0]: "))
a.append(input("a[1]: "))
a.append(input("a[2]: "))

# 続いて、リストをソートして、表示してみましょう。
a.sort()
print(a)

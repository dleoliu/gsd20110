import sys

# 各メソッド外で各Aspectのリストを定義
a = []
b = []


def error_exit():
    print("Input error. Positive integer only.")
    sys.exit()


def pos_int_checker(x):
    if x.isdigit() is False:
        error_exit()
    if int(x) < 0:
        error_exit()
    return True


# Aspect 1は第７回ワークショップの解答とだいたい同じ
def a1():
    print("---Aspect 1---")
    print("Please input 5 positive integers for list a[].")
    i = 0
    while i < 5:
        temp = input("a[%d]: " % i)
        pos_int_checker(temp)
        a.append(int(temp))
        i += 1
    a.sort(reverse=True)
    print("-----------------")
    for i in range(len(a)):
        print("a[%d]: %d" % (i, a[i]))
    print()


# 注意：isdigit()はマイナスの整数(-1など)を整数と判定しない．
def a2():
    print("---Aspect 1---")
    print("Please input positive integers for list b[].")
    i = 0
    while True:
        temp = input("b[%d]: " % i)
        if temp.isdigit() is False:
            break
        b.append(int(temp))
        i += 1
    b.sort(reverse=True)
    print("-----------------")
    for i in range(len(b)):
        print("b[%d]: %d" % (i, b[i]))
    print()


def main():
    a1()
    a2()


if __name__ == "__main__":
    main()

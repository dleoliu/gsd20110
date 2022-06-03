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


def a1():
    print("---Aspect 1---")
    print("Please input 10 positive integers for list a[].")
    for i in range(10):
        temp = input("a[%d]: " % i)
        pos_int_checker(temp)
        a.append(int(temp))
    a.sort(reverse=True)
    print("a = " + str(a))
    print()


def a2():
    print("---Aspect 2---")
    n = input("Please input a positive integer: ")
    if pos_int_checker(n):
        n = int(n)
    print("Please input %d positive integers for list b[]." % n)
    for i in range(n):
        temp = input("b[%d]: " % i)
        pos_int_checker(temp)
        b.append(int(temp))
    b.sort(reverse=True)
    print("b = " + str(b))
    print()


def a3():
    print("---Aspect 3---")
    odd_flag = False
    odd_b = []
    for c in b:
        if c % 2:
            odd_b.append(c)
            odd_flag = True
    if odd_flag:
        print("Odd numbers in list b[]: " + str(odd_b))
    else:
        print("There is no odd number in list b[].")


def main():
    a1()
    a2()
    a3()


# ↓：もしこのファイルをそのまま実行する時，main()関数を実行することを意味する．
if __name__ == "__main__":
    main()

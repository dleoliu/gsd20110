def isIn(s1, s2):
    if s1 in s2:
        return True
    else:
        return False


def main():
    s1 = input("文字列1> ")
    s2 = input("文字列2> ")
    print("どちらか一方の文字列が他方の文字列内に含まれる？", isIn(s1, s2))


if __name__ == "__main__":
    main()

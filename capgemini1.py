def moveHash(str1, n):
    hash = ""
    letters = ""
    for i in str1:
        if i == '#':
            hash = hash + i
        else:
            letters = letters + i
    return hash+letters


if __name__ == "__main__":
    str1 = input()
    n = len(str1)
    print(moveHash(str1, n))

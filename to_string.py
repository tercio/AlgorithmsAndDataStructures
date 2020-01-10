def toStr(n,base) -> str:

    convertString = "0123456789ABCDEF"

    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n % base]

if __name__ == "__main__":

    print(toStr(1453,16))

    print(toStr(1453,10))

    print(toStr(13,2))
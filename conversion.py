def StrToInt (str):

    # Horner's Rule
    neg = False
    num = 0
    ordZero = ord('0')
    for c in str:
        if c == "-":
            neg = True
        else:
            num *= 10
            num += ord(c) - ordZero

    if neg:
        num = -num

    return num

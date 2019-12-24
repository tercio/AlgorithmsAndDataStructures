# location 2531 - livro

def firstNonRepeated (s):

    charCount = {}
    for c in s:
        if c in charCount:
            charCount[c] = charCount[c] + 1
        else:
            charCount[c] = 1

    for k in charCount:
        if charCount[k] == 1:
            return k

    return nil

if __name__ == "__main__":

    s = "esperandio"
    print ("the first non repeated in %s is %s" % (s,firstNonRepeated(s)))

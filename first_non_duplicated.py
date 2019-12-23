

def first_non_duplicated(s):

    chars_count = {}
    for c in s:
        if c in chars_count:
            chars_count[c] = chars_count[c] + 1
        else:
            chars_count[c] = 1

    char = ''
    for c in chars_count:
        if chars_count[c] == 1:
            char = c
            break

    return char



if __name__ == "__main__":

    s = "find first non duplicated character in a string"
    print ("First non repeated char in \"",s,"\" is ",first_non_duplicated(s),sep='')
    s = "algorithms and data structures"
    print ("First non repeated char in \"",s,"\" is ",first_non_duplicated(s),sep='')

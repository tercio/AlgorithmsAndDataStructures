# Longest Repeated Substring

import fileinput
import sys

def lcp (s1,s2):
    
    i = 0
    while i < len(s1) and i < len(s2):
        if s1[i] != s2[i]:
            break
        i += 1
    
    return i

def lrs (s):
    
    suffix = ['']*len(s)
    for i,_ in enumerate(s):
        suffix[i] = s[i:]
    print ("suffix read")

    suffix.sort()
    print ("suffix sorted")

    lrs_str = ""
    max_len = -1
    for i in range(0,len(s)-1):
        lrs_len = lcp(suffix[i],suffix[i+1])
        if lrs_len > max_len:
            max_len = lrs_len
            lrs_str = suffix[i][:lrs_len]

    print ("lcp done")

    return lrs_str

if __name__ == "__main__":

    #s = "banana"
    #print (lrs(s))

    translation = {'\r\n':''}

    lines = sys.stdin.readlines()
    lines = "".join(lines                                                                                                                                                                                                                                                                                                                                                                               )
    lines = lines.translate(translation)

    print ("input ok")
    print (lrs(lines))




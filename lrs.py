# Longest Repeated Substring

import fileinput
import sys

sg = ""

def lcp (s1,s2):
    
    i = 0
    while i < len(s1) and i < len(s2):
        if s1[i] != s2[i]:
            break
        i += 1
    
    return i


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def sort_suffix(a,b):
    #print (a," ",b," -- ",sg[a:]," ",sg[b:])
    # stcmp like
    if sg[a:] == sg[b:]: return 0
    if sg[a:] > sg[b:]: return 1
    if sg[a:] < sg[b:]: return -1
    

def lrs (s):
    
    #suffix = sorted(s[i:] for i,_ in enumerate(s)) # too slow for moby dick file ~1.2 m chars and worst, we get a kill from s.o. because of memory usage
    #suffix = [s[i:] for i,_ in enumerate(s)]
    #suffix.sort()
    #print (suffix)
    #print (len(suffix))

    suffix = [i for i in range(0,len(s))] # pointer like to the original string, but still slow. 
    print ("pre suffix done")
    #suffix = sorted(suffix,key=lambda key: s[key:])
    suffix.sort(key=cmp_to_key(sort_suffix)) # with this, no problem with memory as we don't create those big arrays, But still very slow!

    print ("suffix read")
    #print (suffix)
    #for pos in suffix:
    #    print (s[pos:],end="")

  
    lrs_str = ""
    max_len = -1
    for i,pos in enumerate(suffix[:-1]):
        lrs_len = lcp(s[suffix[i]:],s[suffix[i+1]:])
        if lrs_len > max_len:
            max_len = lrs_len
            lrs_str = s[pos:pos+lrs_len]

    print ("lcp done")

    return lrs_str

if __name__ == "__main__":

    #s = "banana"
    #print (lrs(s))

    translation = {'\r\n':''}

    lines = sys.stdin.readlines()
    chars = "".join(lines)
    #lines = lines.translate(translation)

    sg = chars
    print ("input ok - #",len(chars)," chars read")
    print (lrs(chars))




# Longest Repeated Substring

#
# Notes about performance:
#  I found the using array or strings slices causes the script to become very, very slow
#  When I had to use then on lcp() or on the for, or on the suffix processing, the time was more than 1 hour 
#  (in fact, I interrupted the script). 
#  Also, using a new array to the suffix array, caused the S.O to kill the script, as the size of the memory
#  used was really big. I preferred to create an suffix array that is only a pointer like to the initial position
#  of each substring (same as the poiter "a" on my longest_duplicate.c)


import fileinput
import sys

sg = ""

def lcp (pos1,pos2):
    
    i = 0
    lena = len(sg) - pos1
    lenb = len(sg) - pos2
    while i < lena and i < lenb:
        if sg[pos1+i] != sg[pos2+i]:
            break
        i += 1
    
    return i


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            #print ("<0")
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            #print (">")
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            #print ("==")
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def sort_suffix_slow(a,b):

    
    #print (a," ",b," -- ",sg[a:]," ",sg[b:])
    # stcmp like
    lenb = len(sg[b:])
    for pos,_ in enumerate(sg[a:]):

        if pos >= lenb: break            
        if sg[a+pos] != sg[b+pos]: break

    if pos >= lenb:
        pos -= 1
    
    #print (" -> ",sg[a+pos]," - ",sg[b+pos])
    #print (" -> ",ord(sg[a+pos]) - ord(sg[b+pos]))

    return ord(sg[a+pos]) - ord(sg[b+pos])


def sort_suffix(a,b):
    #print (a," ",b," -- ",sg[a:]," ",sg[b:])
    # stcmp like

    lena = len(sg) - a
    lenb = len(sg) - b

    pos = 0
    while pos < lena and pos < lenb:

        if pos >= lenb: break            
        if sg[a+pos] != sg[b+pos]: break
        pos += 1

    if pos >= lena:
        pos -= 1
    if pos >= lenb:
        pos -= 1
    
    #print (" -> ",sg[a+pos]," - ",sg[b+pos])
    #print (" -> ",ord(sg[a+pos]) - ord(sg[b+pos]))

    return ord(sg[a+pos]) - ord(sg[b+pos])    

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
    i = 0
    slen = len(suffix)
    while i < slen-1:
        
        lrs_len = lcp(suffix[i],suffix[i+1])
        if lrs_len > max_len:
            max_len = lrs_len
            lrs_str = s[suffix[i]:suffix[i]+lrs_len]

        i += 1

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




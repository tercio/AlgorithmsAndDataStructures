
def reverse_string(slist,start,end):

    temp = ""
    while start < end:
        temp = slist[start]
        slist[start] = slist[end]
        slist[end] = temp
        start += 1
        end -= 1

    return slist

def reverse_words(str):

    slist = list(str)

    rstr = reverse_string(slist,0,len(slist)-1)
    start = 0
    end = 0
    for idx,c in enumerate(rstr):
        if c == " ":
            end = idx - 1
            reverse_string(rstr,start,end)
            start = idx + 1

    end = idx
    reverse_string(rstr,start,end)

    return "".join(rstr)

def longest_palindrome(s:str)->str:
    
    if s == None or len(s) < 1: 
        return ""

    start = 0
    end = 0
    for i,_ in enumerate(s):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i+1 )
        mlen = max(len1, len2)
        #print (i," ",mlen," ",start," ",end)
        if mlen > end - start:
            start = int(i - (mlen - 1) / 2)
            end = int(i + mlen / 2)
    
    return s[start: end +1]


def expandAroundCenter(s,left ,right):
    L = left
    R = right

    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1
    
    return R - L - 1


if __name__ == "__main__":

    s = "cbbd"
    print (s," : ",longest_palindrome(s))    

    s = "xabax"
    print (s," : ",longest_palindrome(s))

    s = "xabay"
    print (s," : ",longest_palindrome(s))    

    s = "abxsewr"
    print (s," : ",longest_palindrome(s))

    s = "babad"
    print (s," : ",longest_palindrome(s))    

    s = "tresabba"
    print (s," : ",longest_palindrome(s))    

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print (s," : ",longest_palindrome(s))        
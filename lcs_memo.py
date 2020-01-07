# Longest Common Subsequence
# Memoized Version
# https://www.techiedelight.com/longest-common-subsequence/

lookup = {}

def lcs (s1,s2,m,n):

    if m < 0 or n < 0:
        return 0

    key = m,"|",n
    if key not in lookup:

        if s1[m] == s2[n]:
            lookup[key] = lcs(s1,s2,m-1,n-1) + 1
        else:
            lookup[key] = max(  lcs(s1,s2,m-1,n),
                                lcs(s1,s2,m,n-1))

    return lookup.get(key)    


if __name__ == "__main__":

    s1 = "abcbdab"
    s2 = "bdcaba"
    m = len(s1) - 1
    n = len(s2) - 1
    print ("LCS for ",s1," & ",s2," is: ",lcs(s1,s2,m,n))


    s1 = "sao paulo"
    s2 = "em sao abc paulo sp"
    m = len(s1) - 1
    n = len(s2) - 1
    print ("LCS for ",s1," & ",s2," is: ",lcs(s1,s2,m,n))

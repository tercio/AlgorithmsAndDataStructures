# Longest Common Subsequence
# Bottom up Version
# https://www.techiedelight.com/longest-common-subsequence/


def lcs (s1,s2,m,n):

    lookup = [[0]*(n+1)]*(m+1)

    for i in range (1,m+1):

        for j in range (1,n+1):

            if s1[i-1] == s2[j-1]:
                lookup[i][j] = lookup[i -1][j - 1] + 1
            else:
                lookup[i][j] = max(lookup[i -1][j],lookup[i][j - 1])

    print (lookup)
    return lookup[i][j]


if __name__ == "__main__":

    s1 = "abcbdab"
    s2 = "bdcaba"
    m = len(s1)
    n = len(s2)
    print ("LCS for ",s1," & ",s2," is: ",lcs(s1,s2,m,n))


    s1 = "sao paulo"
    s2 = "em sao paulo sp"
    m = len(s1)
    n = len(s2)
    print ("LCS for ",s1," & ",s2," is: ",lcs(s1,s2,m,n))
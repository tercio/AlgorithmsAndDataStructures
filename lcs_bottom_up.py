# Longest Common Subsequence
# Bottom up Version
# https://www.techiedelight.com/longest-common-subsequence/



def lcs (s1,s2,m,n):

    substr = ""

    #lookup = [[0]*(n+1)]*(m+1)
    lookup = [[0 for x in range(n+1)] for x in range(m+1)]
    build  = [['' for x in range(n+1)] for x in range(m+1)]
    

    for i in range (1,m+1):

        for j in range (1,n+1):

            if s1[i-1] == s2[j-1]:
                lookup[i][j] = lookup[i -1][j - 1] + 1
                build[i][j] = 'r' 
            else:
                l = lookup[i -1][j]
                u = lookup[i][j - 1]
                lookup[i][j] = max(l,u)
                build[i][j] = 'l' if l > u else 'u'

    #print (lookup)
    #print (build)

    x = m
    y = n

    
    while x >= 0 and y >= 0:
        if build[x][y] == 'r':
            substr += s1[x-1] # -1 só pq a tabela inicia em 1 e nao em zero
            x -= 1
            y -= 1
        elif build[x][y] == 'u':
            y -= 1 
        elif build[x][y] == 'l':
            x -= 1
        else:
            break

    substr = substr[::-1]
    return (substr,lookup[i][j])


if __name__ == "__main__":

    s1 = "axbxxxdx"
    s2 = "abcd"
    m = len(s1)
    n = len(s2)

    substr,ls = lcs(s1,s2,m,n)
    print ("LCS for ",s1," & ",s2," is: ",substr," with len= ",ls)

    s1 = "--s-a-o- - -p-a-u-l-o-"
    s2 = "em s.a.o p.a.u.l.o sp"
    m = len(s1)
    n = len(s2)
    substr,ls = lcs(s1,s2,m,n)
    print ("LCS for ",s1," & ",s2," is: ",substr," with len= ",ls)

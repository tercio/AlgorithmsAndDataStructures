# Dynamic Programming
# Exemplo do tutorital de DP do Topcoder

def max_apples(a):

    
    n = len(a)
    m = len(a[0])
    s = [[0,0,0]]*n

    #print (n," ",m," ",a," ",s)

    for i in range (0,n):
        for j in range(0,m):
            ii = s[i-1][j] if i > 0 else 0
            jj = s[i][j-1] if j > 0 else 0
            maxij = max(ii,jj)
            s[i][j] = a[i][j] + maxij

    #print (s)

    return s[n-1][m-1]

if __name__ == "__main__":


    apples = [  [2,4,5],
                [5,7,6],
                [3,2,8],
                [6,4,2],
                [2,3,1]
            ]
    
    print (max_apples(apples))
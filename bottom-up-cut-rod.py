# Dynamic Programming 
# Exemplo no livro Introduction to Algorithms - pagina 366


def bottom_up_cut_rod(p,n):

    r = [0 for x in range (n + 1)]

    #print (p)
    #print (r)
    for j in range (1,n+1):
        q = -5000

        for i in range (1,j+1):
            #print ("q: {} i: {} p[i]: {} j:{} r[j-i]: {}  -  p[i]+r[j-i]: {}".format(q,i,p[i],j,r[j-i],p[i] + r[j - i]))
            q = max(q, p[i] + r[j - i])
        
        r[j] = q
        #print ("--- ",r,"\n")

    #print (r)
    return r[n]

def cut_rod(p,n):
    memo = {}
    r = cut_rod_aux(p,n,memo)
    print (memo)
    return r

def cut_rod_aux(p,n,memo):

    if n in memo:
        return memo[n]

    if n <= 0:
        return 0

    q = -5000
    for i in range (1,n+1):
        q = max(q,p[i] + cut_rod_aux(p,n-i,memo))

    memo[n] = q

    return q


if __name__ == "__main__":

    p = [0,1,5,8,9,10,17,17,20,50,30,30,35,45,50,55,58,60,63,64,68,70,72,74,54]

    n = 4
    print("(Bottom-up) N: ",n," gets a revenue equals to ",bottom_up_cut_rod(p,n))
    print("(Recursive) N: ",n," gets a revenue equals to ",cut_rod(p,n))

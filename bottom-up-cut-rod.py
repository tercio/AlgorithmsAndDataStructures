# Dynamic Programming 
# Exemplo no livro Introduction to Algorithms - pagina 366


def bottom_up_cut_rod(p,n):

    r = [0] * (n + 1)
    print (p)
    print (r)
    for j in range (1,n+1):
        q = -5000
        for i in range (1,j+1):
            print ("q: {} i: {} p[i]: {} j:{} r[j-i]: {}  -  p[i]+r[j-i]: {}".format(q,i,p[i],j,r[j-i],p[i] + r[j - i]))
            q = max(q, p[i] + r[j - i])
        r[j] = q
        print ("--- ",r,"\n")

    print (r)
    return r[n]


if __name__ == "__main__":

    p = [0,1,5,8,9,10,17,17,20,24,30]

    n = 4
    print("N: ",n," gets a revenue equals to ",bottom_up_cut_rod(p,n))
